import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()
#connection
def connection():
    conn=psycopg2.connect(
        host=os.getenv("host"),
        port=os.getenv("port"),
        database=os.getenv("database"),
        user=os.getenv("user"),
        password=os.getenv("password")
    )
    print("Connected Successfully!")
    return conn



connection()