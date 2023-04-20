# Deploy a Python (Django) app to Azure with Managed Identity 

This Python app is a simple restaurant review application using the [Django](https://www.djangoproject.com/) framework. The app uses Azure App Service, Azure Database for PostgreSQL relational database service, and Azure Storage. When deployed, Azure managed identity allows the web app hosted in App Service to connect to the database and storage resources without the need to specify sensitive connection info in code or environment variables.

This sample app can be run locally and then deployed to Azure, hosted in a fully managed Azure App Service. For more information on how to use this web app, see the  [Overview: Deploy a Python web app to Azure with managed identity](https://docs.microsoft.com/azure/developer/python/tutorial-python-managed-identity-01).

If you need an Azure account, you can [create on for free](https://azure.microsoft.com/free/).

A Flask sample application with similar functionality is at https://github.com/Azure-Samples/msdocs-flask-web-app-managed-identity.

## Requirements

The [requirements.txt](./requirements.txt) has the following packages:

| Package | Description |
| ------- | ----------- |
| [Django](https://pypi.org/project/Django/) | Web application framework. |
| [pyscopg2-binary](https://pypi.org/project/psycopg-binary/) | PostgreSQL database adapter for Python. |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from .env file and set them as environment variables. In this sample app, environment variables describe how to connect to the database and storage resources. Because managed identity is used no sensitive information is included in environment variables. <br><br> This package is used in the [manage.py](./manage.py) file to load environment variables. |
| [whitenoise](https://pypi.org/project/whitenoise/) | Static file serving for WSGI applications, used in the deployed app. <br><br> This package is used in the [azureproject/production.py](./azureproject/production.py) file, which configures production settings. |
| [azure-blob-storage](https://pypi.org/project/azure-storage/) | Microsoft Azure Storage SDK for Python |
| [azure-identity](https://pypi.org/project/azure-identity/) | Microsoft Azure Identity Library for Python |

## DefaultAzureCredential

The [DefaultAzureCredential](https://docs.microsoft.com/python/api/azure-identity/azure.identity.defaultazurecredential) is used in the [views.py](./restaurant_review/views.py) file. For example:

```python
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

azure_credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)
blob_service_client = BlobServiceClient(
    account_url=account_url,
    credential=azure_credential)
```

The DefaultAzureCredential is also used to get a token for PostgreSQL in the [get_token.py](./azureproject/get_token.py) file when running in Azure.

```python
azure_credential = DefaultAzureCredential()
token = azure_credential.get_token("https://ossrdbms-aad.database.windows.net")
conf.settings.DATABASES['default']['PASSWORD'] = token.token
```


