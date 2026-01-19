# Snapshot Cleanup Lambda

## Purpose
Automatically deletes EBS snapshots that:
- Have no associated volume
- Reference a deleted volume
- Are attached to volumes not connected to running EC2 instances

## Safety Controls
- Dry-run mode via environment variable
- Tag-based protection (`DoNotDelete`)
- Least-privilege IAM permissions

## Trigger
Scheduled via CloudWatch Events (daily)

## Cost Impact
Prevents accumulation of unused EBS snapshots, reducing monthly AWS storage costs.
