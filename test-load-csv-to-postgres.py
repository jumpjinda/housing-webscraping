import psycopg2
import csv


# in postgres version 14, we need to use with syntax to do state
# login to default database and create database name "housing"
user = "postgres"
password = "soulfunkjazz88"
host = "localhost"
conn = psycopg2.connect(dbname="postgres", user=user,
                        password=password, host=host)

# make cursor auto commit (like confirm our command)
conn.autocommit = True

with conn.cursor() as cur:
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'housing'")
    exists = cur.fetchone()
    if not exists:
        cur.execute('CREATE DATABASE housing')