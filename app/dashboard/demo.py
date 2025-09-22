import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_HOST = "127.0.0.1"
DB_NAME = "mydb"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_PORT = 5433

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    cursor = conn.cursor()
    print("Connected to the database successfully!")

    # Insert data into DEMO table
    query = sql.SQL("INSERT INTO {table} (name) VALUES (%s)").format(
        table=sql.Identifier("DEMO")  # Use exact table name
    )
    cursor.execute(query, ("test",))  # Tuple for values
    conn.commit()
    print("Data inserted successfully!")

except psycopg2.Error as e:
    print("Error connecting or executing:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
