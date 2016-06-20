# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient
from bson.code import Code


class MongoAggregationMoviesTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = None
        self.db = None
        self.movies = None


    def tearDown(self): 
        self.mongoclient.close()

    """
    Trouver l'actor avec le plus grand nombre de films à son actif
    """
    @unittest.skip('Remove to play this test')
    def testFindActorWithLargestPorfolio(self):
        pipeline = []
        result = self.movies.aggregate(pipeline)
        self.assertEqual(result['result'][0]['_id'], 'Robert De Niro')
        self.assertEqual(result['result'][0]['number_of_movies'], 9)

if __name__ == '__main__':
    unittest.main()
