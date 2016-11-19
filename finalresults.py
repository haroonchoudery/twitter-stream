from __future__ import absolute_import, print_function, unicode_literals
import sys
from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

if __name__ == "__main__":
	argword = sys.arg[1]

	print argword
	# cur.execute("SELECT word, count from Tweetwordcount;")
	# records = cur.fetchall()
	# for rec in records:
	#    print "word = ", rec[0]
	#    print "count = ", rec[1], "\n"
	# conn.commit()

conn.close()