# Part 2: AWS Setup & Exploration

## Objective

The objective of this task is to gain hands-on experience with core AWS services and understand fundamental cloud concepts. This includes configuring AWS credentials securely, launching an EC2 instance, creating an S3 bucket, and learning about regions, availability zones, IAM, and S3 access permissions.

---

## Prerequisites

- AWS Account
- Internet Connection
- AWS Management Console Access
- AWS CLI Installed
- IAM User with appropriate permissions

---

# Task 1: AWS Account Verification

Logged into the AWS Management Console and verified access to the following services:

- IAM
- EC2
- S3

This confirmed that the AWS account was active and ready for use.

---

# Task 2: IAM User Creation

Created a dedicated IAM user instead of using the root account.

### Steps Performed

1. Opened IAM Dashboard.
2. Navigated to **Users**.
3. Selected **Create User**.
4. Created a new IAM user.
5. Attached the required permissions.
6. Completed user creation.

---

# Task 3: AWS Access Key Creation

Generated programmatic access credentials for AWS CLI usage.

### Steps Performed

1. Opened IAM User.
2. Selected **Security Credentials**.
3. Chose **Create Access Key**.
4. Selected **CLI Access**.
5. Generated:
   - Access Key ID
   - Secret Access Key

These credentials were stored securely.

---

# Task 4: AWS CLI Configuration

Configured AWS CLI using the generated IAM credentials.

### Command Used

```bash
aws configure
```

### Configuration Details

```text
AWS Access Key ID
AWS Secret Access Key
Default Region Name
Default Output Format
```

### Verification Command

```bash
aws sts get-caller-identity
```

The command successfully returned IAM user details, confirming successful configuration.

---

# Task 5: EC2 Instance Launch

Created a Free Tier EC2 instance.

### Configuration

| Setting        | Value             |
| -------------- | ----------------- |
| AMI            | Amazon Linux 2023 |
| Instance Type  | t2.micro          |
| Storage        | 8 GB              |
| Security Group | SSH Allowed       |

### Steps Performed

1. Opened EC2 Dashboard.
2. Selected **Launch Instance**.
3. Configured instance settings.
4. Generated a key pair.
5. Launched the instance.

---

# Task 6: EC2 Instance Connection

Connected to the running EC2 instance using EC2 Instance Connect.

### Verification Command

```bash
uname -a
```

The successful output confirmed access to the Linux server.

# Task 7: S3 Bucket Creation

Created an Amazon S3 bucket for cloud storage.

### Configuration

| Setting       | Value           |
| ------------- | --------------- |
| Bucket Type   | General Purpose |
| Public Access | Blocked         |
| Versioning    | Disabled        |

### Steps Performed

1. Opened S3 Dashboard.
2. Selected **Create Bucket**.
3. Entered bucket name.
4. Chose AWS region.
5. Kept public access blocked.
6. Created the bucket.

---

# Task 8: File Upload to S3

Uploaded a sample text file to verify object storage functionality.

### Uploaded File

```text
sample.txt
```

### Steps Performed

1. Opened the S3 bucket.
2. Selected **Upload**.
3. Chose sample.txt.
4. Uploaded successfully.

---

# Conceptual Understanding

## What is an AWS Region?

An AWS Region is a geographical location where AWS hosts its cloud infrastructure and services.

### Examples

- Mumbai (ap-south-1)
- Singapore (ap-southeast-1)
- US East (us-east-1)

### Benefits

- Reduced latency
- Compliance with local regulations
- Better disaster recovery planning

---

## What is an Availability Zone?

An Availability Zone (AZ) is an isolated data center within an AWS Region.

### Example

```text
ap-south-1a
ap-south-1b
ap-south-1c
```

### Benefits

- High availability
- Fault tolerance
- Improved reliability

---

## Difference Between Public and Private Access in S3

### Private Access

Objects are accessible only to authorized AWS users.

#### Common Use Cases

- Application data
- Customer records
- Backups
- Sensitive documents

### Public Access

Objects can be accessed by anyone on the internet.

#### Common Use Cases

- Public website assets
- Downloadable files
- Static website hosting

### Best Practice

Keep **Block Public Access** enabled unless public access is specifically required.

---

## What is IAM?

IAM (Identity and Access Management) is an AWS service used to manage authentication and permissions.

### IAM Allows Users To

- Create users
- Create groups
- Assign permissions
- Secure AWS resources

---

## What is an IAM Role?

An IAM Role provides temporary permissions to AWS services without requiring access keys.

### Examples

- EC2 accessing S3
- Lambda accessing DynamoDB
- ECS accessing CloudWatch

### Advantages

- Improved security
- No hardcoded credentials
- Easier permission management

---

# Outcome

Successfully completed AWS Setup & Exploration by:

- Creating and configuring an IAM user
- Generating AWS access keys
- Configuring AWS CLI
- Launching a Free Tier EC2 instance
- Connecting to the EC2 server
- Creating an S3 bucket
- Uploading files to S3
- Understanding Regions, Availability Zones, IAM Roles, and S3 access controls

This task established the AWS environment required for the upcoming Python and cloud integration tasks.
