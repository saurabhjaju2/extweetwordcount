
# extweetwordcount
W205 exercise_2
How to Run the Application:

## Setting up the system
Create ab EC2 instance
Configure the instance to have:
1. postgres
2. python 2.7.3 
3. virtualenv
4. redis installed

also install the following python packages if not installed
1. Numpy
2. Tweepy
3. Streamparse
4. psycopg2
5. psycopg2 extensions
6. re
7. Queue
8. itertools

and any other dependency if the python programs throw a dependency error.

## Executing the project
Steps:
1. Clone the github repo
2. Create a new project on streamparse called Tweetwordcount.
3. Move the files above to your streamparse project, renaming it to Tweetwordcount. 
4. To run finalresults.py and get a wordcount, type python finalresults.py followed by the word you are looking for.
5. To run histogram.py. use the following format " python histogram.py 3 7
