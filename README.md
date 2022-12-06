# GoodReads Containerized FastAPI Application

![Continuous Integration/Deployment with Github Actions](https://github.com/nogibjj/fastapi-project/actions/workflows/main.yml/badge.svg)

![CodeBuild Badge](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoibUR3bGs0eXQwQ1VGNWd1YkJHNXc4dkZ2R2dUK2NZMy80Z2U2cDFLLzVlYVR3S0RBajZzNTJUYzZNeGtkZ20rcVdJcHdMcTg3ZE9XMmFISlJpTWNFakVvPSIsIml2UGFyYW1ldGVyU3BlYyI6IjFtV2lkMVBBbXplS1BGemQiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

## Overview

This FastAPI application, developed on Github Codespace and deployed through AWS Elastic Container Registry, CodeBuild, and App Runner, queries a database of goodreads books and provides its users with information on books' authors, publisher, rating, and number of reviews. The application provides Swagger UI documentation and allows users to query books by their title. Continuous Integration and Continuous Deployment are performed through Github Actions and pushes the latest images to AWS ECR, which automatically deploys through AWS CodeBuild and App Runner. 

## Project Workflow

![workflow](https://user-images.githubusercontent.com/60377132/205476572-9dd5724a-911e-4330-9186-d33cd2c59392.png)

## Operation Manual

The Application allows users to query books by going to the documentation and looking up the title of the book using the POST method. Users can also look up information about the book using GET method through the book's index number in the data.

Here is a screenshot of the Swagger UI documentation that automatically comes with FastAPI, making it one of the most powerful API application software.

<img width="1417" alt="Screen Shot 2022-12-06 at 12 36 00 PM" src="https://user-images.githubusercontent.com/60377132/205993926-e1f0d49c-6c28-4913-a93a-37b6bef04738.png">

Users can enter in the book they are looking to query and receive a JSON payload that looks something like this:  

```
{
  "title": "Poor People",
  "book_id": 45639,
  "authors": "William T. Vollmann",
  "average rating": 3,
  "publisher": "Ecco",
  "isbn code": "0439785960",
  "language code": "eng",
  "number of pages": 652,
  "number of ratings posted": 2095690,
  "number of reviews posted": 27591
}
```

### Project Automation

Continuous Integration and Deployment of the application relies on AWS CodeBuild, AWS Elastic Container Registry, and AWS AppRunner. CodeBuild is configured such that AWS will install the required softwares, lint, test, and deploy the docker container on ECR. AWS App Runner, which is hooked up to ECR, will then automatically deploy the updated container in the registry. 

When a new version of the code is pushed to GitHub, CodeBuild triggers and sends a newer version of the container to ECR.

<img width="1067" alt="Screen Shot 2022-12-06 at 12 59 27 PM" src="https://user-images.githubusercontent.com/60377132/205999047-12c96348-462e-473b-9250-bcaaa5768307.png">

<img width="1120" alt="Screen Shot 2022-12-06 at 12 58 48 PM" src="https://user-images.githubusercontent.com/60377132/205998826-a19808db-2b96-483f-b431-6f5f9c7aacbc.png">

### Replication

You can replicate the results and the application by cloning this GitHub repo and running ```python app.py```. 