# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient


class MongoDBTest(unittest.TestCase):

    #  Ce test permet de vérifier que nous pouvons nous connecter et que la base grades existe
    def testThatListDbWorks(self):
        mongoclient = MongoClient()
        databases = mongoclient.database_names()
        self.assertTrue('grades' in databases)
            

     #  Ce test permet de vérifier la connexion à une collection
    def testThatWeCanConnectToACollection(self):
        mongoclient = MongoClient()
        mediatheque = mongoclient.mediatheque
        movies = mediatheque.movies

        self.assertEqual(movies.find().count(), 350)

 
if __name__ == '__main__':
    unittest.main()


