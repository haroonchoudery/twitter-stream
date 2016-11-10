from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

cur = conn.cursor()

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
        
        if (word in Counter) == False:
            cur.execute("INSERT INTO Tweetwordcount (word,count) \
                  VALUES (word, 1)");
            conn.commit()
        else:
            cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (count+1, word))
            conn.commit()
        #Update
        #Assuming you are passing the tuple (uWord, uCount) as an argument
        
        

        


        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

conn.close()