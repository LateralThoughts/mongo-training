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


    #  Trouver la plus grande affluence (nombre de requêtes par jour) pour l'url http://www.lateral-thoughts.com
    # avec le framework d'aggrégation
    def testFindHighestHitsForUrl(self):
        match = {'$match' : {"url" : 'http://www.lateral-thoughts.com'}} 
        projection = {'$project' : 
                        {
                            '_id' : '$url', 
                            'date' : {
                                'y' : {'$year' : '$date'},
                                'm' : {'$month' : '$date'},
                                'd' : {'$dayOfMonth' : '$date'}
                            }
                        }
                      }
        group = {'$group' : {
                                '_id' : {
                                    'p' : '$_id',
                                    'y' : '$date.y',
                                    'm' : '$date.m',
                                    'd' : '$date.d'
                                }, 
                                'hits' : {'$sum' : 1}
                            }
                }
        
        sort = {"$sort" : {"hits" : -1}}
        limit = {"$limit" : 1}
        result = self.hits.aggregate([match, projection, group, sort, limit])
        self.assertEqual(result['result'][0]['hits'], 66)
        self.assertEqual(result['result'][0]['_id']['y'], 2012)
        self.assertEqual(result['result'][0]['_id']['m'], 3)
        self.assertEqual(result['result'][0]['_id']['d'], 23)

    #  Trouver la plus grande affluence (nombre de requêtes par jour) pour l'url http://www.lateral-thoughts.com
    # avec un map reduce
    def testFindHighestHitsForUrlWithMapReduce(self):
        mapper = Code("""
                       function() {
                        var key = {
                                    url : this.url,
                                    y : this.date.getFullYear(),
                                    m : this.date.getMonth()+1,
                                    d : this.date.getUTCDate(),
                                   };
                        emit(key,1);
                    }
                       """)
        reducer = Code("""
                       function(url, values) {
                            var res = 0;
                            return Array.sum(values)
                        }
                       """)


        result = self.db.hits.map_reduce(mapper, reducer, "hits_per_url")
        self.assertEqual(result.find({'_id.url':'http://www.lateral-thoughts.com'}).count(), 372)
        stats = result.find({'_id.url':'http://www.lateral-thoughts.com'}).sort([("value", -1)]).limit(1)
        for stat in stats:
            self.assertEqual(66, stat['value'])
            self.assertEqual(2012, stat['_id']['y'])
            self.assertEqual(3, stat['_id']['m'])
            self.assertEqual(23, stat['_id']['d'])

if __name__ == '__main__':
    unittest.main()
