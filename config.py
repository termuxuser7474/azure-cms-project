import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Azure Blob Storage Configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsimages1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'GXgNYFobRd80M4VFxs8Rpmna/AP7CLBkxEpbOdLlRsrKiKqCygm8BYL4vu6KlEow6jEvGeTMANXU+ASt2kbV8Q=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Azure SQL Database Configuration
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-server-12.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or r'M@ss@@@786'
    
    # URL-encode the password to handle special characters like '@'
    encoded_password = quote_plus(SQL_PASSWORD)
    
    # Finalized Connection String
    # THE FIX: Added :1433 immediately after {SQL_SERVER} to force the correct routing
    # Change from 'ODBC+Driver+17+for+SQL+Server' to '{ODBC Driver 18 for SQL Server}'
# And add TrustServerCertificate=yes
    SQLALCHEMY_DATABASE_URI = (
        f'mssql+pyodbc://{SQL_USER_NAME}:{encoded_password}@{SQL_SERVER}:1433/{SQL_DATABASE}'
    '?driver=ODBC+Driver+18+for+SQL+Server&LoginTimeout=30&encrypt=yes&TrustServerCertificate=yes'
     )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    CLIENT_SECRET = "J.N8Q~B36P1BTmRFTC2GMlZqh2ow58HKcDeOrbtS"
    AUTHORITY = "https://login.microsoftonline.com/common"
    CLIENT_ID = "b0aa7bed-08a1-4cd3-8f30-1dcc23610899"

    REDIRECT_PATH = "/getAToken" 
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"  

    # Fix for Azure HTTPS Proxy issues
    PREFERRED_URL_SCHEME = 'https'