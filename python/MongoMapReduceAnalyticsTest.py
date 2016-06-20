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
    avec un map reduce
    En javascript pour récupérer année/mois/jour sur une date :
    https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Date
    """
    @unittest.skip('Remove to play this test')
    def testFindHighestHitsForUrlWithMapReduce(self):
        mapper = {}
        reducer = {}

        result = None
        self.assertEqual(result.find({'_id.url':'http://www.lateral-thoughts.com'}).count(), 372)
        stats = result.find({'_id.url':'http://www.lateral-thoughts.com'}).sort([("value", -1)]).limit(1)
        for stat in stats:
            self.assertEqual(66, stat['value'])
            self.assertEqual(2012, stat['_id']['y'])
            self.assertEqual(3, stat['_id']['m'])
            self.assertEqual(23, stat['_id']['d'])

if __name__ == '__main__':
    unittest.main()
