import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="127.0.0.1", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

## Creating cursor
cur = conn.cursor()

## Point to remember sys.argv[0] is the python file name 
## and has length 1 i.e the name of the file is word length 1

## fetchone(), fetchmany(), fetchall() to retrive records
## single word argument

if len(sys.argv) == 2:
	word = str(sys.argv[1])
	cur.execute("SELECT word , count FROM Tweetwordcount WHERE word = %s;", (word, ))
	record = cur.fetchone()	
	print(record)

## Only file name provided
elif len(sys.argv) == 1:
	cur.execute("SELECT word, count FROM Tweetwordcount;")
	countTable = cur.fetchall()
	## sorting counts using a lambda function
	sortedTable =sorted(countTable, key = lambda countTable: countTable[0])
	for tup in sortedTable:
		print(tup[0], tup[1])	
else:
	print('Please select a word to search in the tweets or see the complete table')
	print('Use the following format: fileresults.py word or python finalresults.py')
	sys.exit(1)

cur.close()
conn.close()
