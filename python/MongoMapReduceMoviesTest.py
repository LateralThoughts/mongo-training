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
    def testFindActorWithLargestPorfolioWithMapReduce(self):
        mapper = {}
        reducer = {}

        # TODO : utiliser la fonction map_reduce sur la collection movies
        # La collection de sortie doit être "movies_per_actor"
        result = None
        self.assertEqual(result.find().count(), 4346)
        actors = self.db.movies_per_actor.find().sort([("value.count", -1)]).limit(1)
        for actor in actors:
            self.assertEqual('Robert De Niro', actor['_id'])
            self.assertEqual(9, actor['value']['count'])


if __name__ == '__main__':
    unittest.main()
