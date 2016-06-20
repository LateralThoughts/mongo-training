# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient


class MongoCursorTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = MongoClient()
        self.db = self.mongoclient.mediatheque
        self.movies = self.db.movies


    def tearDown(self): 
        self.mongoclient.close()


    # Ce test permet de vérifier le titre du 10eme film trié par note ascendante
    def testThatThe10thScifiMovieOrderedByRatingIsTheExpectedOne(self):
      cursor = self.movies.find({"genres" : "Sci-Fi"}).skip(9).limit(1).sort([("rating",1)])
      for movie in cursor:
        self.assertEqual(movie["title"], 'Space Mutiny')


if __name__ == '__main__':
    unittest.main()
