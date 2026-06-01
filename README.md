# AWS Cloud & Storage Integration Using Python

## Project Overview

This project demonstrates the integration of Python applications with AWS cloud services using Boto3. The implementation focuses on Amazon S3 for data storage and transfer while applying cloud computing concepts, AWS best practices, automation techniques, and secure credential management.

The project covers AWS account setup, EC2 and S3 exploration, file uploads and downloads, automation using modular Python code, and understanding how the same solution can run on Amazon EC2 instances.

---

# Objective

The objective of this project is to:

- Understand AWS cloud services and architecture.
- Work with Amazon S3 using Python and Boto3.
- Implement file upload and download workflows.
- Handle common error scenarios.
- Apply automation and modular programming practices.
- Understand EC2 deployment concepts and IAM role usage.

---

# AWS Services Used

## Amazon S3 (Simple Storage Service)

Amazon S3 is an object storage service used to:

- Store files in the cloud.
- Upload files from local systems.
- Download files from cloud storage.
- Manage and list stored objects.

### Usage in this Project

- Upload CSV files to S3.
- Store large datasets.
- Download files from S3.
- Verify uploaded and downloaded files.

---

## Amazon EC2 (Elastic Compute Cloud)

Amazon EC2 provides virtual servers in the AWS cloud.

### Usage in this Project

- Understanding how Python scripts can run on cloud infrastructure.
- Learning the difference between local execution and cloud execution.
- Exploring IAM role integration with EC2.

---

## IAM (Identity and Access Management)

IAM is used to manage AWS access and permissions.

### Usage in this Project

- Created IAM user credentials.
- Configured AWS CLI access.
- Learned IAM role concepts for EC2 instances.

---

# Project Structure

```text
AWS_Cloud_Storage_Integration_Using_Python/

├── data/
│   ├── sample_data.csv
│   └── large_data.csv
│
├── downloads/
│
├── docs/
│   ├── Cloud_and_AWS_Understanding.md
│   ├── Part2_AWS_Setup_Exploration.md
│   ├── Part3_Python_Boto3_Data_Transfer.md
│   ├── Part4_Automation_and_Logic.md
│   └── Part5_EC2_Context.md
│
├── screenshots/
│
├── scripts/
│   ├── config.py
│   ├── s3_operations.py
│   ├── upload_csv_to_s3.py
│   ├── upload_large_file.py
│   ├── download_from_s3.py
│   ├── verify_file_integrity.py
│   ├── list_s3_files.py
│   ├── upload_file.py
│   ├── download_file.py
│   └── list_files.py
│
├── .gitignore
└── README.md
```

---

# Script Flow

## Upload Workflow

```text
Local CSV File
       │
       ▼
Python Script
       │
       ▼
Boto3
       │
       ▼
Amazon S3 Bucket
```

### Process

1. Read file from local storage.
2. Create S3 client using Boto3.
3. Upload file to S3 bucket.
4. Display upload status.

---

## Download Workflow

```text
Amazon S3 Bucket
       │
       ▼
Python Script
       │
       ▼
Local Downloads Folder
```

### Process

1. Connect to S3 bucket.
2. Download selected file.
3. Save file locally.
4. Verify successful transfer.

---

## File Integrity Verification Workflow

```text
Original File
      │
      ▼
SHA-256 Hash
      │
      ▼
Compare
      │
      ▼
Downloaded File Hash
```

### Purpose

Ensures the downloaded file matches the original file and has not been corrupted during transfer.

---

## Bucket Listing Workflow

```text
Amazon S3 Bucket
       │
       ▼
Boto3
       │
       ▼
Python Script
       │
       ▼
Display Object Names
```

---

# Features Implemented

## Part 1: Cloud & AWS Understanding

Covered:

- Cloud Computing
- IaaS, PaaS, SaaS
- AWS use cases
- EC2 and S3 architecture concepts

---

## Part 2: AWS Setup & Exploration

Completed:

- AWS account setup
- IAM user configuration
- AWS CLI credential configuration
- EC2 instance launch
- S3 bucket creation
- Understanding AWS regions and availability zones
- Understanding public and private S3 access

---

## Part 3: Python + Boto3 Data Transfer

Implemented:

### Upload Operations

- Small CSV upload
- Large CSV upload

### Error Handling

- File not found error
- Invalid AWS credentials
- Bucket access validation

### Download Operations

- Download files from S3
- Verify file integrity
- List bucket contents

---

## Part 4: Automation & Logic

Implemented:

- Parameterized bucket names
- Parameterized file paths
- Parameterized AWS region
- Modular Python functions
- Logging support
- Secure credential handling

---

## Part 5: EC2 Context

Covered:

- Running scripts on EC2
- Local vs EC2 execution
- IAM roles and secure authentication
- Cloud deployment concepts

---

# Assumptions

The following assumptions were made:

- AWS account is active.
- IAM user has required S3 permissions.
- AWS CLI is configured properly.
- Python and Boto3 are installed.
- S3 bucket exists before execution.
- Internet connectivity is available.

---

# Limitations

- Only Amazon S3 operations are implemented.
- Large file uploads are simulated using generated CSV files.
- EC2 execution is explained conceptually.
- Advanced monitoring services such as CloudWatch are not included.
- Multi-region replication is not implemented.

---

# Security Considerations

- AWS credentials are not hardcoded.
- Credentials are managed through AWS CLI configuration.
- IAM best practices were followed.
- Sensitive information is excluded from source code.

---

# Screenshots and Evidence

The project includes screenshots demonstrating:

- IAM user creation
- EC2 instance launch
- S3 bucket creation
- CSV uploads
- Large file uploads
- File downloads
- Logging output
- Bucket listing results

These screenshots are available in the `screenshots` directory.

---

# Technologies Used

- Python 3
- AWS S3
- AWS EC2
- AWS IAM
- AWS CLI
- Boto3 SDK
- Git
- GitHub

---

# Outcome

Successfully designed and implemented a Python-based AWS cloud storage workflow using Amazon S3 and Boto3.

The project demonstrates:

- Cloud computing fundamentals
- AWS service integration
- File transfer automation
- Error handling
- Modular programming
- Secure credential management
- Understanding of EC2 deployment concepts

This project provides practical experience with AWS cloud services and Python-based automation commonly used in real-world cloud environments.
