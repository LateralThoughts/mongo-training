# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient
from bson.code import Code


class MongoAnalyticsTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = MongoClient()
        self.db = self.mongoclient.analytics
        self.hits = self.db.hits


    def tearDown(self): 
        self.mongoclient.close()


    """
    Trouver la plus grande affluence (nombre de requêtes par jour) pour l'url http://www.lateral-thoughts.com
    avec le framework d'aggrégation
    Doc à lire : 
    - $year http://docs.mongodb.org/manual/reference/operator/aggregation/year/
    - $month http://docs.mongodb.org/manual/reference/operator/aggregation/month/
    - $dayOfMonth http://docs.mongodb.org/manual/reference/operator/aggregation/dayOfMonth/
    """
    @unittest.skip('Remove to play this test')
    def testFindHighestHitsForUrl(self):
        pipeline = []
        result = self.hits.aggregate(pipeline)
        self.assertEqual(result['result'][0]['hits'], 66)
        self.assertEqual(result['result'][0]['_id']['y'], 2012)
        self.assertEqual(result['result'][0]['_id']['m'], 3)
        self.assertEqual(result['result'][0]['_id']['d'], 23)


if __name__ == '__main__':
    unittest.main()
