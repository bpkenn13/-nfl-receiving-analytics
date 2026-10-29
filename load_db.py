import getpass
import psycopg

password = getpass.getpass("PostgreSQL password: ")

with psycopg.connect(dbname="nfl_receiving_stats", user="postgres",
                     password=password, host="localhost") as conn:
    with conn.cursor() as cur:
        with open("receiving_weekly.csv", newline="") as f:
            with cur.copy("COPY receiving_games FROM STDIN WITH (FORMAT csv, HEADER true)") as copy:
                copy.write(f.read())

print("Loaded!")