import os
from dotenv import load_dotenv

load_dotenv()

Base_url = os.getenv('BASE_URL')


Key = '?key=qaclick123'
Resource_Post = '/maps/api/place/add/json'
Resource_Get = '/maps/api/place/get/json'
Resource_Put = '/maps/api/place/update/json'
Resource_Delete = '/maps/api/place/delete/json'
