from os import environ 
from dotenv import load_dotenv 

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_DEV') 
    SQLALCHEMY_TRACK_MODIFICATIONS=False 
    
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY') 
    JWT_TOKEN_LOCATION = ['headers']  
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer' 
    