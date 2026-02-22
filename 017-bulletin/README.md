# 📌 Supabase-Powered Real-Time Bulletin Board
[Place holder]
![Graphical Summary](attachments/bulletin.png)

## 📂 Table of Contents
- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Cost Management](#-cost-management)
  - [EC2 Instance Deployment](#ec2-instance-deployment)
  - [Custom VPC & Networking Configuration](#custom-vpc--networking-configuration)
  - [CloudWatch Metrics Collection](#cloudwatch-metrics-collection)
  - [CloudWatch Logs](#cloudwatch-logs)
  - [CloudWatch Alarms & Alert Validation](#cloudwatch-alarms--alert-validation)
  - [Cost Management & Resource Cleanup](#cost-management--resource-cleanup)
- [AWS Lambda - Cost Optimization Automation](#-aws-lambda--cost-optimization-automation)
- [Summary](#-summary)

## 🧠 Overview
[Add a project description – Highlight the technologies: HTML, CSS, JS, Supabase, SQL, JSON, and async APIs.]

## ▶️ Live Demo
[Link to a live demo – Deploy the site on Netlify (or Vercel) so visitors can post and view messages.]
https://realtime-bulletin-board-demo.netlify.app/

[Include screenshots or GIFs – Show the hero page fading out, posting a comment, and the dynamic rendering of posts.]

## 🚨 Cost Management
This section demonstrates system observability and cost-aware monitoring using Amazon CloudWatch. An EC2 instance is deployed inside a custom VPC, application metrics and logs are collected, and alarms are configured to validate automated alerting behavior under load.

### EC2 Instance Deployment

A Python application is deployed to an EC2 instance running inside a custom VPC and subnet. The instance serves as the workload target for monitoring and alert validation.

**EC2 Instance**
![EC2 Instance](attachments/ec2.png)

**EC2 Instance Details**
![EC2 Instance Running](attachments/ec2-2.png)

### Custom VPC & Networking Configuration

A dedicated VPC and subnet are created to isolate the EC2 instance. Routing, security groups, and internet access are explicitly configured to support application execution and monitoring.

**VPC**
![Custom VPC](attachments/vpc.png)

**VPC Details**
![Custom VPC](attachments/vpc-2.png)

**VPC Subnets**
![Subnet](attachments/vpc-subnets.png)

VPC Internet gateway and security groups are demonstrate as well.

**Internet Gateway**
![Internet Gateway](attachments/vpc-internet-gateway.png)

**Internet Gateway Details**
![Internet Gateway Details](attachments/vpc-internet-gateway-2.png)

**Security Groups**
![Security Groups](attachments/vpc-security-groups.png)

### CloudWatch Metrics Collection

Amazon CloudWatch is used to collect EC2 performance metrics, including CPU utilization. Metrics are visualized in near real time while the application workload is running.

A workload-generating Python script is executed to intentionally increase CPU usage and validate metric collection behavior.

**CloudWatch Metrics Overview**
![CloudWatch Metrics Overview](attachments/cloudwatch-metrics.png)

**CloudWatch Metrics Example: CPU Utilization**
![CloudWatch Metrics Example](attachments/cloudwatch-cpu-utilization.png)

### CloudWatch Logs

Application logs are streamed to CloudWatch Logs, enabling centralized visibility into runtime behavior without directly accessing the EC2 instance.

**CloudWatch Log**
![CloudWatch Log](attachments/cloudwatch-log.png)

### CloudWatch Alarms & Alert Validation

A CloudWatch alarm is configured to monitor CPU utilization and trigger when a defined threshold is exceeded. During workload execution, the alarm transitions to the ALARM state, confirming correct configuration and end-to-end monitoring.

**CloudWatch Alarm**
![CloudWatch Alarm](attachments/cloudwatch-alarm.png)
**CloudWatch Alarm Details**
![CloudWatch Alarm Details](attachments/cloudwatch-alarm-2.png)

### Cost Management & Resource Cleanup

After validating metrics, logs, and alarms, all AWS resources are deleted, including the EC2 instance, VPC components, CloudWatch alarms, and log groups. This ensures zero ongoing cost while preserving the configuration and documentation for reproducibility.

## 💻 AWS Lambda – Cost Optimization Automation

In addition to the EC2-based monitoring workflow, this demo includes a serverless AWS Lambda function designed for **ongoing cost optimization**.

This Lambda is intentionally decoupled from the CI/CD and EC2 workload. Its purpose is to demonstrate how **event-driven automation** can be used to continuously control cloud costs without requiring persistent compute.

![Lambda](attachments/lambda-1.png)
![Lambda](attachments/lambda-2.png)

### Purpose
The Lambda identifies and cleans up unused EBS snapshots that:
- Have no associated volume
- Reference deleted volumes
- Are attached to volumes not connected to running EC2 instances

This prevents silent accumulation of snapshot storage costs in dynamic
environments where volumes and instances are frequently created and removed.

### Implementation
- Triggered on a schedule via CloudWatch Events
- Uses least-privilege IAM permissions
- Includes dry-run support and tag-based protection
- Logs all actions to CloudWatch

### Code Location
The Lambda implementation is maintained as a **self-contained subproject** with its own documentation:
([View lambdas](lambdas))

## 💡 Summary

This project demonstrates an end-to-end AWS workflow combining CI/CD automation, infrastructure deployment, system monitoring, and cost-conscious cloud management. A Python application is built and tested through a GitHub-triggered AWS CodeBuild pipeline, deployed to an EC2 instance within a custom VPC, and monitored using Amazon CloudWatch metrics, logs, and alarms. Controlled workload generation is used to validate observability and alerting behavior. All resources are cleaned up after validation to ensure zero ongoing cost, reflecting production-minded cloud engineering practices.






Optional code link – Share a GitHub repo, but remove your Supabase keys (or use environment variables) so the project still works for visitors.

Highlight skills – Call out full-stack integration, database handling, and asynchronous JS logic, showing technical depth without needing a large application.


