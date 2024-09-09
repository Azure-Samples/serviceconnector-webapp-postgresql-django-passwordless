import os
from .settings import *
from .get_token import get_token

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

if 'AZURE_POSTGRESQL_CONNECTIONSTRING' in os.environ:
    # Using PostgreSQL connection string for managed identity
    conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
    conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
    dbhost=conn_str_params['host']
    dbname=conn_str_params['dbname']
    dbuser=conn_str_params['user']
else:
    # DBHOST is only the server name, not the full URL
    # Postgres Flexible server username is DBUSER, not DBUSER@DBHOST
    dbhost = os.environ['DBHOST'] + ".postgres.database.azure.com"
    dbname = os.environ['DBNAME']
    dbuser = os.environ['DBUSER']

# Configure Postgres database; the full username for PostgreSQL flexible server is
# username (not @sever-name).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': dbname,
        'HOST': dbhost,
        'USER': dbuser,
        'PASSWORD': 'set with get_token()' 
    }
}
get_token()
