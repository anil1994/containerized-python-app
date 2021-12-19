# Containerised Application for calculating factorial of a given non-negative integer
This containerised Python application uses Flask. It is a simple example for AWS ECS Demo.

My application listens flask default port 5000.

I can dockerize this flask application by using dockerfile

I can expose my application via Elastic Load Balancer.

Application is deployed to ECS fargate. But I realized that fargate has not free tier. That's why I switch ECS fargate to ECS EC2. 

When I set ec2 as t2.micro spec in order to use free tier, but unfortunately again, it costs to me. That's why I deleted ECS cluster temporarily.
you should be so careful whether AWS resource is free tier or not


http://factorial-597623339.eu-central-1.elb.amazonaws.com/number/5

120

You can change number 5 to any positive integer you want to take factorial

## Infrastructure

AWS CDK (Python) used for Infrastructure as Code (Seperate repository)

* AWS ECR
* AWS ECS

IaC repository:https://github.com/anil1994/aws-iac 

## CICD

 I used Github Actions used for auto building docker image and deploying it to AWS ECS. when my code is on the github, it is so easy to integrate with CI/CD by using github action. There are many predefined github action modules. By referring these modules, I can easily integrate with CI/CD. 
 
 You can find pipeline yml in the .github/workflows/factorial.yml
   
   When your environment has many platforms such as AWS,Google Cloud,Openshift, I suggest you should use jenkins CI/CD tool. Because, Jenkins have so many plugins that integrate with so many platforms (AWS,Azure,Openshift,GKE etc). When our environment has only AWS platform, we can use AWS Codebuild,Codedeploy,Codepipeline resources. Our github account can easily sync to AWS and we can easily integrate our code with  codepipeline.  
