import os
from azure.identity import DefaultAzureCredential
import django.conf as conf

# This is for demo purposes. Consider using Django middleware to hook into req/resp processing.

def get_token():
    if 'WEBSITE_HOSTNAME' in os.environ:   
        # Azure hosted, refresh token that becomes password.
        # Get token for Azure Database for PostgreSQL
        azure_credential = DefaultAzureCredential()
        token = azure_credential.get_token("https://ossrdbms-aad.database.windows.net")
        conf.settings.DATABASES['default']['PASSWORD'] = token.token
    else:
        # Locally, read password from environment variable.
        conf.settings.DATABASES['default']['PASSWORD'] = os.environ['DBPASS']
    return