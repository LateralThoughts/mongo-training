# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient


class MongoCursorTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = None
        self.db = None
        self.movies = None


    def tearDown(self): 
        self.mongoclient.close()


    """
    Ce test permet de vérifier le titre du 10eme film de Science fiction (Sci-Fi) trié par note ascendante
    """
    @unittest.skip('Remove to play this test')
    def testThatThe10thScifiMovieOrderedByRatingIsTheExpectedOne(self):
        query = {}
        cursor = []
        self.assertTrue(cursor.count() > 0)
        for movie in cursor:
            self.assertEqual(movie["title"], 'Space Mutiny')


if __name__ == '__main__':
    unittest.main()
