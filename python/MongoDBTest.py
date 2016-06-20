# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient


class MongoDBTest(unittest.TestCase):

    #  Ce test permet de vérifier que nous pouvons nous connecter et que la base grades existe
    @unittest.skip('Remove to play this test')
    def testThatListDbWorks(self):
        mongoclient = None
        databases = None
        self.assertTrue('grades' in databases)
            

    #  Ce test permet de vérifier la connexion à une collection
    @unittest.skip('Remove to play this test')
    def testThatWeCanConnectToACollection(self):
        mongoclient = None
        mediatheque = None
        movies = None

        self.assertEqual(movies.find().count(), 350)

 
if __name__ == '__main__':
    unittest.main()


