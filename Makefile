install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest test*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	
deploy:
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/p8v3p4h9
	docker build -t deploy-goodreads-fastapi .
	docker tag deploy-goodreads-fastapi:latest public.ecr.aws/p8v3p4h9/deploy-goodreads-fastapi:latest
	docker push public.ecr.aws/p8v3p4h9/deploy-goodreads-fastapi:latest

all:
	make install test format lint deploy