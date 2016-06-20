# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient


class MongoFindTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = MongoClient()
        self.db = self.mongoclient.mediatheque
        self.movies = self.db.movies


    def tearDown(self): 
        self.mongoclient.close()


    #  Ce test d'exemple permet de vérifier que nous avons bien 350 films en base de données
    def testThatDatabaseHas350Movies(self):
        self.assertEqual(self.movies.find().count(), 350)
    

    #  Ce test doit vérifier que nous avons 69 films de 'Crime'
    def testThatMovieWithGenreCrimeAre69(self):
        self.assertEqual(self.movies.find({"genres" : 'Crime'}).count(), 69)

    #  Ce test ne doit récupérer que le champ 'title' de la base
    def testProjectionOnTitle(self):
        movie = self.movies.find_one({}, {"title": 1})
        self.assertTrue( 'title' in movie)
        self.assertEqual(len(movie), 2)

    # Ce test doit vérifier que nous avons 118 films avec une note comprise entre 7 et 8
    def testRatingBetween7And8(self):
        self.assertEqual(self.movies.find(
            {
           "rating":{ "$gte": 7 },
           "rating":{ "$lte": 8 }
           }).count(), 118)

    #   Ce test vérifie que nous avons 24 films de 'Comedy' et de 'Romance' (simultanèment)
    def testAllMovieComedyAndRomance(self):
        self.assertEqual(self.movies.find({"genres" : {'$all' : ['Comedy', 'Romance']}}).count(), 24)

    #   Ce test vérifie que nous avons 243 films qui ne sont ni des 'Comedy', ni des films de 'Romance'
    def testAllMovieNotComedyAndRomance(self):
        self.assertEqual(self.movies.find({"genres" : {"$nin" : ['Comedy', 'Romance']}}).count(), 243)

     #  Ce test vérifie que nous avons 53 films de sciences fiction, ou dont l'un des acteurs est Morgan Freeman
    def testAllMovieScienceFictionOrWithMorganFreeman(self):
        self.assertEqual(self.movies.find({"$or" : [{"genres" : "Sci-Fi"}, {'actors' : 'Morgan Freeman'}]}).count(), 53)

     #  Ce test vérifie que nous avons 335 films dont le champ also_known_as existe
    def testAllMoviesWithFieldAlsoKnownAs(self):
        self.assertEqual(self.movies.find({"also_known_as" : {"$exists" : 1}}).count(), 335)

     #  Ce test vérifie que nous avons 21 films tournés à New York
    def testMoviesLocationMatchingNewYork(self):
        self.assertEqual(self.movies.find({"filming_locations" : {"$regex" : 'new york', '$options': 'i'}}).count(), 21)



if __name__ == '__main__':
    unittest.main()



