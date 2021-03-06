# Deploying-ML-model-to-Azure-Kubernetes-Service

### Preriquisites:
1. An Azure Account

### Steps to follow:
1. Create a workspace [here is how](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace#create-a-workspace).(skip this step if you already have created a workspace)
2. Go to [Azure Notebooks](https://notebooks.azure.com), Sign in using Azure account.
3. Go to My Projects -> New Project.
4. Create a new Notebook file to train your model.(you can skip this step if you have a registered model in your workspace)
5. In another Notebook, create a new AKS cluster and deploy model to it.
6. To call this web service using scoring uri, get scoring uri and authentication key(primary) using below:
```
service = Webservice(workspace=ws, name='your-service')
scoring_uri = service.scoring_uri
primary_key, secondary_key = service.get_keys()
```
You can also call service using curl as below:
```
curl -X POST <your scoring uri> --header "Content-Type:application/json" -d '{"data": [ 0.03807591,  0.05068012,  0.06169621,  0.02187235, -0.0442235 , -0.03482076, -0.04340085, -0.00259226,  0.01990842, -0.01764613]}' -H 'authorization: Bearer <your key>'
```
and using Azure CLI
```
az rest --method post --uri <your scoring uri> --headers  Content-Type=application/json Authorization='Bearer <your key>' -b '{"data": [ 0.03807591,  0.05068012,  0.06169621,  0.02187235, -0.0442235 , -0.03482076, -0.04340085, -0.00259226,  0.01990842, -0.01764613]}'
```

Quick disclaimer: At the time of writing, I am currently an employee of Intech Process Automation.

Resources:

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-azure-kubernetes-service

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-existing-model

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice.webservice(class)?view=azure-ml-py#deploy-from-model-workspace--name--models--image-config--deployment-config-none--deployment-target-none--overwrite-false-

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-consume-web-service
