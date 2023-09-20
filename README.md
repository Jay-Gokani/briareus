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

`docker run -p 5000:5000 briareus_v1`

Pushing the Docker image
In the below, username is 'jaygokani' and repo is 'briareus'. The tag is to your choice.

```
docker login -u jaygokani
docker tag briareus_v1 jaygokani/briareus:v1
docker push jaygokani/briareus:v1
```

If building for amd64:

```
docker buildx build --platform=linux/amd64 -t briareus-amd64-v1 .
docker tag briareus-amd64-v1 jaygokani/briareus:amd64
docker push jaygokani/briareus:amd64
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

`helm install briareus-helm briareus-helm --dry-run`

Once happy, install it 
```
helm install briareus-helm briareus-deployment
kubectl get svc
minikube service briareus-service
```

### Azure
Two installations are needed
```
brew update && brew install azure-cli
brew install Azure/kubelogin/kubelogin
```

AKS cluster is created via the UI for initial test

To connect to the cluster, firstly login to the Azure account via the CLI

`az login`

Set the cluster subscription. The subscription ID can be found on the cluster config on the Azure UI

`az account set --subscription 4c746f57-54e8-4929-bfb7-31d9564d1d24`

Download cluster credentials

`az aks get-credentials --resource-group test-clust_group --name test-cluster`

Authenticate with kubelogin plugin

`kubelogin convert-kubeconfig -l azurecli`

Now run some kubectl commands for testing

`kubectl get deployments --all-namespaces=true`

NAMESPACE     NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
kube-system   coredns              2/2     2            2           25m
kube-system   coredns-autoscaler   1/1     1            1           25m
kube-system   konnectivity-agent   2/2     2            2           25m
kube-system   metrics-server       2/2     2            2           25m

Deploy the Helm chart on the AKS cluster

```
helm install briareus-helm briareus-helm --dry-run
helm install briareus-helm briareus-helm
```

If needing to uninstall
```
helm list
helm uninstall briareus-helm-v1
```

See if the resources built 

```
kubectl get svc
kubectl get po
```


helm install briareus-helm-v3 briareus-helm --dry-run