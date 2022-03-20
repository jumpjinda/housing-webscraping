def load_csv_to_postgres(database, table):
    import psycopg2
    import csv
    
    
    user = "postgres"
    password = "soulfunkjazz88"
    host = "localhost"

    # in postgres version 14, we need to use with syntax to do state
    # login to default database and create database name "housing"
    conn = psycopg2.connect(dbname="postgres", user=user,
                            password=password, host=host)

    # make cursor auto commit (like confirm our command)
    conn.autocommit = True

    # check if database housing does exist then not recreate
    with conn.cursor() as cur:
        cur.execute(
            "SELECT 1 FROM pg_catalog.pg_database WHERE datname = '" + database + "'")
        exists = cur.fetchone()
        if not exists:
            cur.execute("CREATE DATABASE " + database)

    conn.close()

    # login to "housing" database, create "weather" table and upload "weather.csv" to "weather" table
    conn = psycopg2.connect(dbname="housing", user=user,
                            password=password, host=host)

    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute("CREATE TABLE " + table + "(price_usd integer, price_baht bigint,\
                     bed integer, bath integer,sqft integer, sq_wah double precision,\
                     house_type varchar, address varchar, link varchar)")

    with conn.cursor() as cur:
        with open('housing-webscraping-to-postgress-mongodb\output-csv\housing_' + table + '.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                cur.execute(
                    "INSERT INTO " + table + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

    # confirm that data has loaded into "weather" table by querying
    with conn.cursor() as cur:
        sql = "SELECT count(*) FROM" + table + ";"
        cur.execute(sql)
        result = cur.fetchone()
        print(table, "table has", result[0], "rows")

    conn.close()


# load_csv_to_postgres("housing", "ca")
