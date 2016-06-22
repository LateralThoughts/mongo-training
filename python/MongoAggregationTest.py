# -*- coding: utf-8 -*-
import unittest
import pymongo
from datetime import datetime
from pymongo import MongoClient


class MongoWriteTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = MongoClient()
        self.db = self.mongoclient.zips
        self.zips = self.db.zips

    def tearDown(self): 
        self.mongoclient.close()


    #  Ce test d'exemple permet de vérifier que nous avons bien 29467 zipcode en base de données
    def testThatDatabaseHasZipcodes(self):
        self.assertEqual(self.zips.find().count(), 29467)

    #  Quelle est la ville dont l'un des quartiers (code postal) a la plus grande population (utiliser uniquement skip limit et sort)
    def testFindLargestZipCodeAmongstCity(self):
        sort = {"$sort" : {"pop" : -1}}
        limit = {"$limit" : 1}
        result = self.zips.aggregate([sort, limit])
        self.assertEqual(result['result'][0]['city'], 'CHICAGO')


    #  Même question que précedemment mais en normalisant le nom de la ville dans l'id
    #  par exemple : chicago IL - zipcode
    def testFindLargestCityWithNormalizedName(self):
        sort = {"$sort" : {"pop" : -1}}
        limit = {"$limit" : 1}
        project = {"$project" : {
                                   "_id" : {
                                        "$concat" : [{"$toLower" : "$city"}, ' ', '$state', ' - ', '$_id'] 
                                   }, 
                                   "pop" : 1
                               }
                  }
        result = self.zips.aggregate([sort, limit, project])
        self.assertEqual(result['result'][0]['_id'], 'chicago IL - 60623')


    # Quelle est la ville dont l'un des quartiers (code postal) a la plus grande population uniquement dans l'état de New York (NY)
    def testFindLargestZipCodeAmongstCityOfNewYork(self):
        sort = {"$sort" : {"pop" : -1}}
        limit = {"$limit" : 1}
        match = {"$match" : { "state" : 'NY' }}
        result = self.zips.aggregate([match, sort, limit])
        self.assertEqual(result['result'][0]['city'], 'BROOKLYN')


    # Trouver l'état avec le plus de quartier
    def testStateWithTheLargestNumberOfZipCodes(self):
        group = {"$group" : {'_id' : '$state', 'number_of_zipcode' : {'$sum' : 1}}}
        sort = {"$sort" : {"number_of_zipcode" : -1}}
        limit = {"$limit" : 1}
        result = self.zips.aggregate([group, sort, limit])
        self.assertEqual(result['result'][0]['_id'], 'TX')
        self.assertEqual(result['result'][0]['number_of_zipcode'], 1676)


    # Trouver le second état avec le plus de quartier
    def testSecondStateWithTheLargestNumberOfZipCodes(self):
        group = {"$group" : {'_id' : '$state', 'number_of_zipcode' : {'$sum' : 1}}}
        sort = {"$sort" : {"number_of_zipcode" : -1}}
        skip = {'$skip' : 1};
        limit = {"$limit" : 1}
        result = self.zips.aggregate([group, sort, skip, limit])
        self.assertEqual(result['result'][0]['_id'], 'NY')
        self.assertEqual(result['result'][0]['number_of_zipcode'], 1596)


    #  Trouver l'état avec la plus grande population
    def testStateWithLargestPopulation(self):
        group = {"$group" : {'_id' : '$state', 'total_pop' : {'$sum' : "$pop"}}}
        sort = {"$sort" : {"total_pop" : -1}}
        limit = {"$limit" : 1}
        result = self.zips.aggregate([group, sort, limit])
        self.assertEqual(result['result'][0]['_id'], 'CA')
        self.assertEqual(result['result'][0]['total_pop'], 29760021)


    #  Quelle est la plus grande ville de l'état de New York (sans utiliser skip et limit mais avec first ou last)
    def testLargestCityInNewYork(self):
        match = {"$match" : { "state" : 'NY' }}
        groupByCity = {"$group" : {'_id' : {"state" : '$state', "city" : "$city"}, 'pop_by_city' : {'$sum' : "$pop"}}}
        sort = {"$sort" : {"pop_by_city" : -1}}
        findLargest = {"$group" : {'_id' : "$_id.state", 'largest_city' : {'$first' : "$_id.city"}, 'largest_pop' : {'$first' : "$pop_by_city"}}}
        result = self.zips.aggregate([match, groupByCity, sort, findLargest])
        self.assertEqual(result['result'][0]['largest_city'], 'BROOKLYN')
        self.assertEqual(result['result'][0]['largest_pop'], 2300504)


    #  Quelle est la moyenne de population d'une ville dans l'état de New York (NY)
    def testAvgPopulationByCityInNewYork(self):
        match = {"$match" : { "state" : 'NY' }}
        groupByCityAndState = {"$group" : {'_id' : {"state" : '$state', "city" : "$city"}, 'pop_by_city' : {'$sum' : "$pop"}}}
        findAverage = {"$group" : {'_id' : "$_id.state", 'avg_city_pop' : {'$avg' : "$pop_by_city"}}}
        result = self.zips.aggregate([match, groupByCityAndState, findAverage])
        self.assertEqual(round(result['result'][0]['avg_city_pop']), 13122)

if __name__ == '__main__':
    unittest.main()
