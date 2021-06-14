import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv('DB_URL', 'sqlite:///./store.db')
V1 = '/v1/api'
