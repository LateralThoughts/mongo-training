# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient


class MongoAdvancedFindTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = None
        self.db = None
        self.grades = None


    def tearDown(self): 
        self.mongoclient.close()


    """  
    Ce test d'exemple permet de vérifier que nous avons bien 280 notes en base de données
    Ce test doit passer si les fonctions setup et teardown sont correctes
    """
    @unittest.skip('Remove to play this test')
    def testThatDatabaseHas280Grades(self):
        self.assertEqual(self.grades.find().count(), 280)
    

    """
    Vous devez avoir 77 documents contenant 3 notes exactements
    """
    @unittest.skip('Remove to play this test')
    def testThatWeHave77LinesWith3Grades(self):
        query={}
        self.assertEqual(self.grades.find(query).count(), 77)

    """
    Ce test doit vérifier que toutes les notes ont des examens
    """
    @unittest.skip('Remove to play this test')
    def testNumberOfGradesWithExam(self):
        query={}
        self.assertEqual(self.grades.find(query).count(), 280)


    """
    Ce test doit vérifier que tous les documents contenant 
    des examens dont la note est > 60 sont de 117
    """
    @unittest.skip('Remove to play this test')
    def testNumberOfGradesWithExamGreaterThan60(self):
        query={}
        self.assertEqual(self.grades.find(query).count(), 117)

    """
    Ce test utilise une projection pour ne renvoyer qu'une seule note par document
    Le tableau "scores" ne doit donc avoir qu'un seul élément dans le résultat
    """
    @unittest.skip('Remove to play this test')
    def testWeCanRetrieveOnlyOneScorePerGrade(self):
        query={}
        projection = {}
        grade = self.grades.find_one(query, projection)
        self.assertTrue( 'scores' in grade)
        self.assertEqual(len(grade['scores']), 1)

if __name__ == '__main__':
    unittest.main()