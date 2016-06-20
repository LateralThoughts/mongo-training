import bottle

import pymongo
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


def random_status():
	return choice([200,404,500,301,302,403])

def random_url():
	return choice(['http://www.hopwork.com/profile',
				   'http://www.google.com',
				   'http://www.hopwork.com/landing',
				   'http://www.hopwork.com/search',
				   'http://www.lateral-thoughts.com',
				   'http://hugo.developpez.com'])	
	
	
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def randip():
    not_valid = [10,127,169,172,192]
 
    first = randrange(1,256)
    while first in not_valid:
		first = randrange(1,256)
 
    ip = ".".join([str(first),str(randrange(1,256)),str(randrange(1,256)),str(randrange(1,256))])
    return ip

d1 = datetime.datetime.strptime('1/1/2012 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.datetime.strptime('1/1/2013 4:50 AM', '%m/%d/%Y %I:%M %p')	
	
connection_string = "mongodb://localhost"
connection = pymongo.Connection(connection_string, safe=True)
db = connection.analytics
hits = db.hits



for i in range(0, 100000):
	hit = {"ip": randip(), 
			"date": random_date(d1, d2),
			"status": random_status(), 
			"size":randint(0,50000), 
			"url": random_url(),
			"request" : choice(['GET', 'POST', 'HEAD', 'PUT'])
		   }


	hits.insert(hit)
