import bottle

from pymongo import MongoClient
import cgi
import re
import datetime
import random
import hmac
import user
import sys
from random import randrange
from random import choice
from random import randint
from datetime import timedelta
import uuid
from loremipsum import generate_paragraph

d1 = datetime.datetime.strptime('1/1/2012 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.datetime.strptime('1/1/2016 4:50 AM', '%m/%d/%Y %I:%M %p')

connection_string = "mongodb://localhost"
connection = MongoClient(connection_string)
db = connection.blog
posts = db.posts

all_tags = posts.distinct("tags")

def random_text():
	sentences_count, words_count, paragraph = generate_paragraph(5)
	return paragraph

def random_uid(string_length=10):
	"""Returns a random string of length string_length."""
	random = str(uuid.uuid4()) # Convert UUID format to a Python string.
	random = random.upper() # Make all characters uppercase.
	random = random.replace("-","") # Remove the UUID '-'.
	return random[0:string_length] # Return the random string.


def random_status():
	return choice([200,404,500,301,302,403])

def random_tag():
	return choice(all_tags)

def random_date(start, end):
	delta = end - start
	int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
	random_second = randrange(int_delta)
	return start + timedelta(seconds=random_second)


for i in range(0, 100000):

	post = {"title": random_uid(),
			"author": 'machine',
			"body": random_text(),
			"permalink":random_uid(),
			"tags": [random_tag()],
			"comments": [
				{"author" : 'machine', "body" : random_text()},
				{"author" : 'machine', "body" : random_text()}
			],
			"date": random_date(d1, d2)}

	posts.insert(post)
