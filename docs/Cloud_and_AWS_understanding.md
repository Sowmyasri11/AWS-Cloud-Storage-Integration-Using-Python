# Cloud Computing Basics

## 1. What is Cloud Computing?

Cloud computing is the delivery of computing services such as servers, storage, databases, networking, and software over the internet.

Instead of buying and maintaining physical hardware, users can access these resources on demand and pay only for what they use.

### Benefits
- Cost savings
- Scalability
- High availability
- Faster deployment
- Easy access from anywhere

---

## 2. Difference Between IaaS, PaaS, and SaaS

| Service Model | Full Form | What the User Manages | Example |
|--------------|-----------|----------------------|---------|
| IaaS | Infrastructure as a Service | Operating system, applications, and data | AWS EC2 |
| PaaS | Platform as a Service | Applications and data | Google App Engine |
| SaaS | Software as a Service | Only uses the software | Gmail, Microsoft 365 |

### Simple Understanding
- **IaaS**: Rent virtual machines and infrastructure.
- **PaaS**: Rent a platform to develop and deploy applications.
- **SaaS**: Use ready-made software through the internet.

---

## 3. Why AWS is Used and Common Real-World Use Cases

AWS (Amazon Web Services) is a cloud platform that provides a wide range of services for computing, storage, databases, networking, analytics, and security.

### Why AWS is Used
- Reliable and secure
- Scalable resources
- Pay-as-you-go pricing
- Global availability
- Large number of cloud services

### Common Real-World Use Cases
- Hosting websites and web applications
- Storing files, images, and videos
- Running databases
- Data backup and disaster recovery
- Big data and analytics
- Machine learning and AI applications
- Mobile and enterprise applications

---

## 4. Purpose of EC2 and S3 in a Cloud Architecture

### EC2 (Elastic Compute Cloud)

EC2 provides virtual servers in the cloud.

#### Uses
- Hosting websites
- Running applications
- Performing data processing tasks
- Running backend services and APIs

### S3 (Simple Storage Service)

S3 is an object storage service used to store and retrieve files.

#### Uses
- Storing images, videos, and documents
- Application backups
- Data archiving
- Static website hosting
- Data storage for analytics and machine learning

### EC2 and S3 Together

A common cloud architecture uses:
- EC2 to run the application
- S3 to store files and application data

Example:
A photo-sharing application can run on EC2 while all uploaded photos are stored in S3.
