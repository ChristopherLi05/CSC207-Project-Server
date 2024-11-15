import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_URL')}/?retryWrites=true&w=majority")
db = client["dev"]
