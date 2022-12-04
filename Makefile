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
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 258567528781.dkr.ecr.us-east-1.amazonaws.com
	docker build -t fastapi-deploy .
	docker tag fastapi-deploy:latest 258567528781.dkr.ecr.us-east-1.amazonaws.com/fastapi-deploy:latest
	docker push 258567528781.dkr.ecr.us-east-1.amazonaws.com/fastapi-deploy:latest

all:
	make install test format lint deploy