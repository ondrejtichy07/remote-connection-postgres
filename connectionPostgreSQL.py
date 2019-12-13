import psycopg2
import os

# Environment variable - nano .bash_profile - export DB_*****="*****"
DB_NAME= os.environ.get('DB_NAME')
DB_USER= os.environ.get('DB_USER')
DB_PASSWORD= os.environ.get('DB_PASSWORD')

def command(hostname, database, user, password, cmd):
    try:
        conn = psycopg2.connect(
            "dbname='{}' user='{}' host={} password='{}'".format(database, user, hostname, password))
        print("Successfully connected to {} database hosted on IP: {}".format(database, hostname).upper())
    except Exception as err:
        print("I am unable to connect to the {} database hosted on IP: {}".format(database, hostname).upper())
        print(err)

    cur = conn.cursor()

    try:
        cur.execute(cmd)
        rows = cur.fetchall()
        listToString = ''.join([str(elem) for elem in rows])
        print(listToString)
    except Exception as err:
        print(err)


command('192.168.0.234', DB_NAME, DB_USER, DB_PASSWORD, 'SELECT version();')
