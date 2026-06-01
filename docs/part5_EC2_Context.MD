# Part 5: EC2 Context (Conceptual + Optional Hands-on)

## Objective

The objective of this task is to understand how Python and Boto3 scripts can be executed on Amazon EC2 instances, compare local execution with cloud-based execution, and learn how IAM roles can securely replace access keys when running applications on AWS.

---

# Introduction

In previous tasks, Python scripts were executed from a local machine to interact with Amazon S3 using Boto3.

The same scripts can also be executed from an Amazon EC2 instance. This approach is commonly used in real-world cloud environments where applications run on cloud servers instead of personal computers.

---

# Running Python Scripts on EC2

## Overview

An Amazon EC2 instance is a virtual server in the AWS cloud. It can be configured with Python, Boto3, and other required software to execute the same scripts developed locally.

### Local Environment

```text
Local Computer
│
├── Python
├── Boto3
├── AWS Credentials
└── Amazon S3
```

### EC2 Environment

```text
EC2 Instance
│
├── Python
├── Boto3
├── IAM Role
└── Amazon S3
```

---

## Typical Steps to Run Scripts on EC2

### Step 1: Connect to the EC2 Instance

```bash
ssh -i key.pem ec2-user@public-ip
```

### Step 2: Verify Python Installation

```bash
python3 --version
```

### Step 3: Install Boto3

```bash
pip3 install boto3
```

### Step 4: Copy Project Files

The project files can be copied using Git or SCP.

Example:

```bash
git clone <repository-url>
```

### Step 5: Execute the Python Script

```bash
python3 upload_file.py
```

The script executes in the same way as it does on the local machine.

---

# Difference Between Running Scripts Locally and on EC2

| Feature       | Local Machine                         | EC2 Instance                 |
| ------------- | ------------------------------------- | ---------------------------- |
| Location      | Personal Computer                     | AWS Cloud Server             |
| Availability  | Available only when system is running | Can run 24/7                 |
| Scalability   | Limited resources                     | Easily scalable              |
| Maintenance   | User-managed                          | AWS-managed infrastructure   |
| Security      | Uses local credentials                | Can use IAM Roles            |
| Accessibility | Local network dependent               | Accessible through AWS cloud |

---

## Local Execution Workflow

```text
Local Machine
      │
      ▼
Python Script
      │
      ▼
Amazon S3
```

The script runs from the user's computer and accesses AWS services using configured credentials.

---

## EC2 Execution Workflow

```text
EC2 Instance
      │
      ▼
Python Script
      │
      ▼
Amazon S3
```

The script runs from an AWS cloud server and can access AWS services directly.

---

# IAM Roles and Access Keys

## Access Keys Approach

In earlier tasks, AWS credentials were configured using:

```bash
aws configure
```

This creates credential information on the local machine.

Example:

```text
Access Key ID
Secret Access Key
```

The Python scripts use these credentials to authenticate with AWS.

---

## Limitations of Access Keys

- Credentials must be stored securely.
- Credentials can be exposed accidentally.
- Key rotation must be managed manually.
- Increased security risk if credentials are hardcoded.

---

# IAM Roles

An IAM Role is a secure AWS identity that provides temporary permissions to AWS resources.

Instead of storing credentials inside code or configuration files, permissions are attached directly to the EC2 instance.

---

## IAM Role Workflow

```text
EC2 Instance
      │
      ▼
IAM Role
      │
      ▼
Amazon S3
```

When the Python script runs:

```python
import boto3

s3 = boto3.client("s3")
```

AWS automatically provides temporary credentials through the attached IAM Role.

No access keys are required.

---

# Advantages of IAM Roles

## Improved Security

No secret keys are stored in source code or configuration files.

---

## Automatic Credential Management

AWS automatically generates and rotates temporary credentials.

---

## Easier Administration

Permissions can be modified in IAM without changing application code.

---

## Industry Best Practice

Most production AWS applications running on EC2 use IAM Roles instead of access keys.

---

# Real-World Example

Consider a data processing application running every day.

### Without IAM Role

```text
EC2
 └── Access Key
 └── Secret Key
 └── Python Script
```

Credentials must be manually managed.

### With IAM Role

```text
EC2
 └── IAM Role
 └── Python Script
```

AWS automatically handles authentication.

This is the preferred approach in professional cloud environments.

---

# Concepts Learned

## What is EC2?

Amazon EC2 (Elastic Compute Cloud) is a virtual server service provided by AWS.

It allows users to run applications in the cloud without managing physical hardware.

---

## Why Run Applications on EC2?

- High availability
- Scalability
- Reliability
- Cloud-based execution
- Easy integration with AWS services

---

## Why Use IAM Roles?

- Better security
- No hardcoded credentials
- Temporary credentials
- Easier permission management

---

# Outcome

Successfully understood:

- How Python and Boto3 scripts can be executed on an EC2 instance.
- The differences between running scripts locally and running them on EC2.
- How IAM Roles can securely replace AWS access keys.
- Why IAM Roles are considered a cloud security best practice.

This task provided an understanding of how AWS applications are typically deployed and secured in real-world cloud environments.
