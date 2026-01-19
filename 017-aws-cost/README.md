# AWS Cost Optimization – EBS Snapshot Cleanup

## Problem
Unused and orphaned EBS snapshots accumulate over time and
increase AWS storage costs, especially in environments with
frequent instance and volume churn.

## Solution
A scheduled AWS Lambda function automatically identifies and
deletes EBS snapshots that:
- Have no associated volume
- Reference deleted volumes
- Are attached to volumes not connected to running EC2 instances

## Architecture
- AWS Lambda
- Amazon EC2 (EBS metadata only)
- CloudWatch Events (schedule)
- IAM (least privilege)
- CloudWatch Logs

## Safety Controls
- Dry-run mode via environment variables
- Tag-based protection (`DoNotDelete`)
- No permissions to modify EC2 instances or volumes

## Workflow
1. CloudWatch triggers Lambda on a schedule
2. Lambda enumerates snapshots and volumes
3. Snapshot eligibility is evaluated
4. Eligible snapshots are deleted (or logged in dry-run)
5. Actions are logged to CloudWatch

## Cost Impact
Prevents silent growth of snapshot storage costs.
Designed for continuous, low-cost enforcement.

## Improvements
- Retention window configuration
- Slack or SNS notifications
- Metrics on estimated savings
