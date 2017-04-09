import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

### Checking for a proper call
if len(sys.argv) != 3:
	print('Please use the format: python histogram.py num1 num2')    
	sys.exit(1)

### Storing input arguments
k1 =sys.argv[1]
k2 =sys.argv[2]
## range is specified in the input arguments
## checking if the range is valid

if (int(k1)>int(k2)):
	print('Invalid range! : First arg must be smaller than the second arg')
	sys.exit(1)

conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="127.0.0.1", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur =conn.cursor()


cur.execute("SELECT word, count FROM Tweetwordcount WHERE count>= %s and count <= %s;" % (k1,k2) )

countTable = cur.fetchall()
for tup in countTable:
	print(tup[0], tup[1])

cur.close()
conn.close()
