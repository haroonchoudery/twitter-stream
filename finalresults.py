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
	if len(sys.argv) > 1:
		argword = sys.argv[1]
	else:
		argword = None

	cur.execute("SELECT word, count from Tweetwordcount WHERE word ~ '^[a-zA-Z]+'")
	records = cur.fetchall()

	if not argword:
		for rec in records:
			print(rec)
	else:
		for rec in records:
			if rec[0] == argword:
			    print("Total number of occurences of '%s': %s" % (rec[0], rec[1]))


	
	conn.commit()

conn.close()