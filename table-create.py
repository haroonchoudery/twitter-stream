import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tweetwordcount')
cur.execute('''CREATE TABLE Tweetwordcount
    (word TEXT PRIMARY KEY NOT NULL,
    count INT NOT NULL);''')
conn.commit()
conn.close()