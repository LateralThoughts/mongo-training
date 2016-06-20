# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient


class MongoFindTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = None
        self.db = None
        self.movies = None


    def tearDown(self): 
        pass


    """
    Ce test d'exemple permet de vérifier que nous avons bien 350 films en base de données
    Seul les fonctions setup et teardown sont testés ici
    """
    @unittest.skip('Remove to play this test')
    def testThatDatabaseHas350Movies(self):
        self.assertEqual(self.movies.find().count(), 350)
    

    """
    Ce test doit vérifier que nous avons 69 films de 'genres' 'Crime'
    """
    @unittest.skip('Remove to play this test')
    def testThatMovieWithGenreCrimeAre69(self):
        query = {}
        self.assertEqual(self.movies.find(query).count(), 69)

    """
    Ce test ne doit récupérer que les champs 'title' et '_id' pour un document
    Nous utilions ici find_one qui ne renvoie qu'un document et nous vérifions que le nombre de propriété 
    est égal à 2 : 'title' et '_id'
    """
    @unittest.skip('Remove to play this test')
    def testProjectionOnTitle(self):
        query = {}
        projection = {}
        movie = self.movies.find_one(query, projection)
        self.assertTrue( 'title' in movie)
        self.assertEqual(len(movie), 2)

    """
    Ce test doit vérifier que nous avons 4 films avec une note comprise entre 9 (exclus)
    et 10 inclus
    """
    @unittest.skip('Remove to play this test')
    def testRatingBetween9And10(self):
        query = {}
        self.assertEqual(self.movies.find(query).count(), 4)

    """
    Ce test vérifie que nous avons 24 films de 'Comedy' et de 'Romance' (simultanement)
    """
    @unittest.skip('Remove to play this test')
    def testAllMovieComedyAndRomance(self):
        query = {}
        self.assertEqual(self.movies.find(query).count(), 24)

    """
    Ce test vérifie que nous avons 243 films qui ne sont ni des 'Comedy', ni des films de 'Romance'
    """
    @unittest.skip('Remove to play this test')
    def testAllMovieNotComedyAndRomance(self):
        query = {}
        self.assertEqual(self.movies.find(query).count(), 243)

    """
    Ce test vérifie que nous avons 53 films de sciences fiction, ou dont l'un des acteurs est Morgan Freeman
    """
    @unittest.skip('Remove to play this test')
    def testAllMovieScienceFictionOrWithMorganFreeman(self):
        query = {}
        self.assertEqual(self.movies.find(query).count(), 53)

    """
    Ce test vérifie que nous avons 335 films dont le champ also_known_as existe
    """
    @unittest.skip('Remove to play this test')
    def testAllMoviesWithFieldAlsoKnownAs(self):
        query = {}
        self.assertEqual(self.movies.find(query).count(), 335)

    """
    Ce test vérifie que nous avons 21 films tournés à New York (utiliser le champ filming_locations)
    """
    @unittest.skip('Remove to play this test')
    def testMoviesLocationMatchingNewYork(self):
        query = {}
        self.assertEqual(self.movies.find(query).count(), 21)



if __name__ == '__main__':
    unittest.main()



