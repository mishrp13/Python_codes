# IAC with AWS CFT

1. Infrastructure as Code (IaC) with AWS

User → IaC Template → AWS

The user defines infrastructure requirements.

The IaC tool (like CloudFormation Template (CFT) or Terraform) acts as a middleman between the user and AWS.

AWS then provisions resources based on the instructions.

Role of Cloud Templates

Templates (written in JSON or YAML) capture infrastructure definitions.

They provide declarative, version-controlled configuration.

Templates are then translated into API calls to AWS services.

AWS CLI vs. CloudFormation/Terraform

AWS CLI:

Good for quick tasks.

Useful for running short commands and immediate results.

CloudFormation / Terraform:

Designed for managing large-scale infrastructure.

Ideal for creating complex architectures (VPCs, route tables, load balancers, EC2 instances, etc.).

Ensures consistency and repeatability.


-------------------

AWS CloudFormation (CFT) – Key Features

2. Infrastructure as Code (IaC)

Defines AWS resources in JSON or YAML templates.

Ensures infrastructure is declarative, version-controlled, and repeatable.

3. Drift Detection

CloudFormation can detect when the actual AWS resources deviate from what’s defined in the template.

Example: If you created EC2 + S3 via CFT, but your colleague accidentally deleted versioning on S3 → CFT will notify you of this drift.

Ways to Create CFT Stacks

AWS CLI: Upload or manage stacks using CLI commands.

AWS Management Console (UI):

Define everything in a Stack (the unit of deployment in CFT).

Must specify Resources (what to create) and their Parameters (configurations/inputs).


4. For creating Cloud formation template we have to go to AWS and search CFT and there
we have to create stack .

5. For creating Stack we can use designer template that is visually appealing but it's better to go for writing yaml file and then download there and create a stack.

6. while creating stack, we can enable versioning that will help in drift detection that is one of the features of CFT.

7. once someone made changes with the stack that you created and you have enable the versioning then you will get to know what changes have been made with drift detection.
