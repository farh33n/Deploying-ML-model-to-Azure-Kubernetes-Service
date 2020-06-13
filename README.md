# Deploying-ML-model-to-Azure-Kubernetes-Service

### Preriquisites:
1. An Azure Account

### Steps to follow:
1. Create a workspace [here is how](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace#create-a-workspace)
2. Go to [Azure Notebooks](https://notebooks.azure.com), Sign in using Azure account.
3. Go to My Projects -> New Project.(you can skip 3-4 if you have pretrained model)
4. Create a new Notebook file to train your model.
5. Go to Azure portal, existing-workspace -> compute -> compute clusters -> new
5. In same Notebook, create a new AKS cluster and deploy model to it.

Quick disclaimer: At the time of writing, I am currently an employee of Intech Process Automation.

Resources:

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-azure-kubernetes-service

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-existing-model

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-existing-model

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice.webservice(class)?view=azure-ml-py#deploy-from-model-workspace--name--models--image-config--deployment-config-none--deployment-target-none--overwrite-false-
