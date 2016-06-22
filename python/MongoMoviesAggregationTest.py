# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient
from bson.code import Code


class MongoMoviesAggregationTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = MongoClient()
        self.db = self.mongoclient.mediatheque
        self.movies = self.db.movies


    def tearDown(self): 
        self.mongoclient.close()

    #  Trouver l'actor avec le plus grand nombre de films à son actif
    def testFindActorWithLargestPorfolio(self):
        unwind = {'$unwind' : '$actors' }
        group = {"$group" : {
                                '_id' : '$actors', 'number_of_movies' : {'$sum' : 1}
                            }
        }
        sort = {"$sort" : {"number_of_movies" : -1}}
        limit = {"$limit" : 1}
        result = self.movies.aggregate([unwind, group, sort, limit])
        self.assertEqual(result['result'][0]['_id'], 'Robert De Niro')
        self.assertEqual(result['result'][0]['number_of_movies'], 9)

    #  Trouver l'actor avec le plus grand nombre de films à son actif
    def testFindActorWithLargestPorfolioWithMapReduce(self):
        mapper = Code("""
                       function() {
                            for (var idx = 0; idx < this.actors.length; idx++) {
                                var key = this.actors[idx];
                                emit(key, this.title);
                            }
                        }
                       """)
        reducer = Code("""
                       function(actor, movies) {
                            movie_list = {count : 0, films : []};
                            for (var i in movies) {
                                movie_list.films = movies[i].concat(movie_list.films);
                                movie_list.count++;
                            }

                            return movie_list;
                        }
                       """)

        result = self.db.movies.map_reduce(mapper, reducer, "movies_per_actor")
        self.assertEqual(result.find().count(), 4346)
        actors = self.db.movies_per_actor.find().sort([("value.count", -1)]).limit(1)
        for actor in actors:
            self.assertEqual('Robert De Niro', actor['_id'])
            self.assertEqual(9, actor['value']['count'])


if __name__ == '__main__':
    unittest.main()
