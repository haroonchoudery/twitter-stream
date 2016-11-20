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
	print(len(sys.argv))

# 	if len(sys.argv) > 2:
# 		mini = sys.argv[1]
# 		maxi = sys.argv[2]
# 	else:
# 		mini = None
# 		maxi = None

# 	cur.execute("SELECT word, count from Tweetwordcount WHERE word ~ '^[a-zA-Z]+' ORDER BY word")
# 	records = cur.fetchall()

# 	if not mini or maxi:
# 		print("Not all arguments given.")
# 	else:
# 		for rec in records:
# 			if rec[1] >= int(mini) and rec[1] <= int(maxi):
# 			    print("'%s': %s" % (rec[0], rec[1]))
	
# 	conn.commit()

# conn.close()