import boto3
import os

ec2 = boto3.client("ec2")

DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"
PROTECTED_TAG = "DoNotDelete"

def lambda_handler(event, context):

    # Get running instance IDs
    active_instance_ids = set()
    paginator = ec2.get_paginator("describe_instances")

    for page in paginator.paginate(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    ):
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                active_instance_ids.add(instance["InstanceId"])

    # Get snapshots
    snapshot_paginator = ec2.get_paginator("describe_snapshots")

    for page in snapshot_paginator.paginate(OwnerIds=["self"]):
        for snapshot in page["Snapshots"]:
            snapshot_id = snapshot["SnapshotId"]
            volume_id = snapshot.get("VolumeId")

            # Skip protected snapshots
            tags = {t["Key"]: t["Value"] for t in snapshot.get("Tags", [])}
            if PROTECTED_TAG in tags:
                continue

            # Snapshot without volume
            if not volume_id:
                delete_snapshot(snapshot_id, "no associated volume")
                continue

            # Check volume
            try:
                vol = ec2.describe_volumes(VolumeIds=[volume_id])["Volumes"][0]

                # Volume not attached
                if not vol["Attachments"]:
                    delete_snapshot(snapshot_id, "volume not attached")
                    continue

                # Volume attached to stopped instance
                attached_instance = vol["Attachments"][0]["InstanceId"]
                if attached_instance not in active_instance_ids:
                    delete_snapshot(snapshot_id, "attached to non-running instance")

            except ec2.exceptions.ClientError as e:
                if e.response["Error"]["Code"] == "InvalidVolume.NotFound":
                    delete_snapshot(snapshot_id, "volume not found")


def delete_snapshot(snapshot_id, reason):
    if DRY_RUN:
        print(f"[DRY-RUN] Would delete {snapshot_id} ({reason})")
    else:
        ec2.delete_snapshot(SnapshotId=snapshot_id)
        print(f"Deleted {snapshot_id} ({reason})")
