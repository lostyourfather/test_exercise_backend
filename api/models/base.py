import os
import databases

DATABASE_URL = f'postgresql://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@db:5432/{os.environ.get("POSTGRES_DB")}'
database = databases.Database(DATABASE_URL)
