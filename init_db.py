import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE_PORT = os.getenv("DATABASE_PORT")

conn = psycopg2.connect(
    database=DATABASE,
    host=HOST,
    user=USER,
    password=PASSWORD,
    port=DATABASE_PORT,
)
cur = conn.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS Testing(id serial PRIMARY KEY, make varchar(100), model varchar(100))"""
)

cur.execute("""INSERT INTO Testing (make, model) VALUES ('Acura', 'Integra')""")

conn.commit()

cur.close()
conn.close()
