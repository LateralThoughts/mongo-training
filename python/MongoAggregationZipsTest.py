# -*- coding: utf-8 -*-
import unittest
import pymongo
from datetime import datetime
from pymongo import MongoClient


class MongoAggregationZipsTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = MongoClient()
        self.db = self.mongoclient.zips
        self.zips = self.db.zips

    def tearDown(self): 
        self.mongoclient.close()


    """
    Ce test d'exemple permet de vérifier que nous avons bien 29467 zipcode en base de données
    """
    @unittest.skip('Remove to play this test')
    def testThatDatabaseHasZipcodes(self):
        self.assertEqual(self.zips.find().count(), 29467)

    """
    Quelle est la ville dont l'un des quartiers (code postal) 
    a la plus grande population (utiliser uniquement skip limit et sort)

    Note : Ici, vous pourriez faire la même chose sans le framework d'aggrégation
    """
    @unittest.skip('Remove to play this test')
    def testFindLargestZipCodeAmongstCity(self):
        pipeline = []
        result = self.zips.aggregate(pipeline)
        self.assertEqual(result['result'][0]['city'], 'CHICAGO')


    """
    Même question que précedemment mais en normalisant le nom de la ville dans un nouveau champ _id qui remplace 
    le précédent champ _id
    par exemple : chicago IL - zipcode
    Doc à lire : 
    - concat : http://docs.mongodb.org/manual/reference/operator/aggregation/concat/
    - toLower : http://docs.mongodb.org/manual/reference/operator/aggregation/toLower/
    """
    @unittest.skip('Remove to play this test')
    def testFindLargestCityWithNormalizedName(self):
        pipeline = []
        result = self.zips.aggregate(pipeline)
        self.assertEqual(result['result'][0]['_id'], 'chicago IL - 60623')


    """
    Quelle est la ville dont l'un des quartiers (code postal) a la plus grande population 
    uniquement dans l'état de New York (NY)
    """
    @unittest.skip('Remove to play this test')
    def testFindLargestZipCodeAmongstCityOfNewYork(self):
        pipeline = []
        result = self.zips.aggregate(pipeline)
        self.assertEqual(result['result'][0]['city'], 'BROOKLYN')


    """
    Trouver l'état avec le plus de zipcode (le plus de document)
    """
    @unittest.skip('Remove to play this test')
    def testStateWithTheLargestNumberOfZipCodes(self):
        pipeline = []
        result = self.zips.aggregate(pipeline)
        self.assertEqual(result['result'][0]['_id'], 'TX')
        self.assertEqual(result['result'][0]['number_of_zipcode'], 1676)


    """
    Trouver le second état avec le plus de zipcode
    """
    @unittest.skip('Remove to play this test')
    def testSecondStateWithTheLargestNumberOfZipCodes(self):
        pipeline = []
        result = self.zips.aggregate(pipeline)
        self.assertEqual(result['result'][0]['_id'], 'NY')
        self.assertEqual(result['result'][0]['number_of_zipcode'], 1596)


    """
    Trouver l'état avec la plus grande population
    """
    @unittest.skip('Remove to play this test')
    def testStateWithLargestPopulation(self):
        pipeline = []
        result = self.zips.aggregate(pipeline)
        self.assertEqual(result['result'][0]['_id'], 'CA')
        self.assertEqual(result['result'][0]['total_pop'], 29760021)


    """
    Quelle est la plus grande ville de l'état de New York (sans utiliser skip et limit mais avec $first ou $last)
    Doc à lire : 
    - $first http://docs.mongodb.org/manual/reference/operator/aggregation/first/
    - $last : http://docs.mongodb.org/manual/reference/operator/aggregation/last/
    """
    @unittest.skip('Remove to play this test')
    def testLargestCityInNewYork(self):
        pipeline = []
        result = self.zips.aggregate(pipeline)
        self.assertEqual(result['result'][0]['largest_city'], 'BROOKLYN')
        self.assertEqual(result['result'][0]['largest_pop'], 2300504)


    """
    Quelle est la moyenne de population d'une ville dans l'état de New York (NY)
    """
    @unittest.skip('Remove to play this test')
    def testAvgPopulationByCityInNewYork(self):
        pipeline = []
        result = self.zips.aggregate(pipeline)
        self.assertEqual(round(result['result'][0]['avg_city_pop']), 13122)

if __name__ == '__main__':
    unittest.main()
