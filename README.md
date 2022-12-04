# GoodReads Containerized FastAPI Application

![Continuous Integration/Deployment with Github Actions](https://github.com/nogibjj/fastapi-project/actions/workflows/main.yml/badge.svg)

## Overview

This FastAPI application, developed on Github Codespace and deployed through AWS Elastic Container Registry, CodeBuild, and App Runner, queries a database of goodreads books and provides its users with information on books' authors, publisher, rating, and number of reviews. The application provides Swagger UI documentation and allows users to query books by their title. Continuous Integration and Continuous Deployment are performed through Github Actions and pushes the latest images to AWS ECR, which automatically deploys through AWS CodeBuild and App Runner. 

## Project Workflow

![workflow](https://user-images.githubusercontent.com/60377132/205476572-9dd5724a-911e-4330-9186-d33cd2c59392.png)

## Operation Manual
