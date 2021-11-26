# cdk-eks

Demo app using CDK to stand up kubernetes resources on EKS


# Setup 

```
git clone ...

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cdk deploy

# run awk eks update-kubeconfig command from CDK Ouputs
```

# Demos

```
kubectl port-forward pods/mypod 8080:8080

curl http://localhost:8080
```
