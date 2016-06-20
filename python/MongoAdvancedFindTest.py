# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient


class MongoAdvancedFindTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = MongoClient()
        self.db = self.mongoclient.grades
        self.grades = self.db.grades


    def tearDown(self): 
        self.mongoclient.close()


    #  Ce test d'exemple permet de vérifier que nous avons bien 280 notes en base de données
    def testThatDatabaseHas280Grades(self):
        self.assertEqual(self.grades.find().count(), 280)
    

     #  Ce test doit vérifier que nous avons 77 enregistrements qui n'ont que 3 notes
    def testThatWeHave77LinesWith3Grades(self):
        self.assertEqual(self.grades.find({"scores" : {"$size" : 3}}).count(), 77)

     #  Ce test doit vérifier que toutes les notes ont des examens
    def testNumberOfGradesWithExam(self):
        self.assertEqual(self.grades.find({"scores.type" : 'exam'}).count(), 280)


     # Ce test doit vérifier que toutes les notes avec examens et > 60 sont de 117
    def testNumberOfGradesWithExamGreaterThan60(self):
        self.assertEqual(self.grades.find(
            {
           "scores":{
              "$elemMatch":{
                 "type":"exam",
                 "score":{
                    '$gt':60
                 }
              }
           }
        }).count(), 117)

     #  Ce test doit vérifier que nous pouvons ne renvoyer qu'une seule note par grade
    def testWeCanRetrieveOnlyOneScorePerGrade(self):
        grade = self.grades.find_one({}, {"scores" : {'$slice' : 1}})
        self.assertTrue( 'scores' in grade)
        self.assertEqual(len(grade['scores']),1)

if __name__ == '__main__':
    unittest.main()