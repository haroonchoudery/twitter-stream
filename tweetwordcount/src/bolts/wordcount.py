from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# #Create a Table
# #The first step is to create a cursor. 
cur = conn.cursor()
# cur.execute('DROP DATABASE IF EXISTS Tcount')
# cur.execute('CREATE DATABASE Tcount')
# cur.execute('DROP TABLE IF EXISTS Tweetwordcount')
# cur.execute('''CREATE TABLE Tweetwordcount
#     (word TEXT PRIMARY KEY     NOT NULL,
#     count INT     NOT NULL);''')
# conn.commit()


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
       

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.

        if (word in self.counts) == False:
            cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s)", (word, 1));
            conn.commit()
        else:
            cur.execute("UPDATE tweetwordcount SET count=count+1 WHERE word=%s", (word))
            conn.commit()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

# conn.close()