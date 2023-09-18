# Briareus
Testing my skills by creating an end-to-end DevOps project, covering containerisation, orchestration, infrastructure as code, cloud computing, and much more. The repo is named after Briareus, a Greek god (a DevOps Engineer) with 100 arms (tools at our disposal)!

## Components
Python: the application is a webpage which runs using the Flask library. The page is built with HTML and CSS.

## Instructions

### Python
Create requirements

`pip3 freeze > requirements.txt`

Run app

`python3 app.py`

### Docker
Build Docker image

`docker build -t briareus_v1 .`

Map local port:docker container port and run container locally

`docker run -p 80:80 briareus_v1`

Pushing the Docker image
In the below, username is 'jaygokani' and repo is 'briareus'. The tag is to your choice.

```
docker login -u jaygokani
docker tag briareus_v1 jaygokani/briareus:[tag]
docker push jaygokani/briareus:[tag]
```

### Minikube & Kubernetes
```
minikube start
kubectl create -f service.yaml
kubectl create -f deployment.yaml
kubectl get svc
minikube service briareus-service
```

A webpage will appear, which is running on the second URL which displays after running the previous command
In this case, it was http://127.0.0.1:50531

### Minikube & Helm 
`minikube start`

Make sure to be in the directory one up from the Helm chart

`helm install briareus-helm briareus-deployment --dry-run`

Once happy, install it 
```
helm install briareus-helm briareus-deployment
kubectl get svc
minikube service briareus-service
```