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
        self.db = self.mongoclient.mediatheque
        self.cds = self.db.cds

    def tearDown(self): 
        self.cds.remove()
        self.mongoclient.close()

    
    #  Ce test d'exemple permet de vérifier que nous avons bien 0 CDs en base de données
    def testThatDatabaseHas0Cds(self):
        self.assertEqual(self.cds.find().count(), 0)        

    #  Ce test permet de vérifier qu'une insertion est prise en compte
    def testInsertWorks(self):
        cd = {"name" : "cd1"}

        self.cds.insert(cd)

        self.assertEqual(self.cds.find().count(), 1)                

    #  Ce test permet de vérifier qu'une insertion par batch est prise en compte
    def testBatchInsert(self):
        cd1 = {"name" : "cd1"}
        cd2 = {"name" : "cd2"}

        bulk = self.cds.initialize_ordered_bulk_op()

        bulk.insert(cd1)
        bulk.insert(cd2)

        bulk.execute()

        self.assertEqual(self.cds.find().count(), 2)   

    #  Ce test permet de vérifier que nous pouvons mettre à jour le nom du CD
    def testUpdateName(self):

        self.testInsertWorks()

        self.cds.update({"name" : "cd1"}, {"$set" : {"name" : "new name"}})

        self.assertEqual(self.cds.find({"name" : "cd1"}).count(), 0)
        self.assertEqual(self.cds.find({"name" : "new name"}).count(), 1)

    #  Ce test permet de vérifier que nous pouvons ajouter un artiste sur le CD et incrémenter un compter nbArtiste par la même occasion
    def testUpdateAndIncr(self):

        self.testInsertWorks()

        self.cds.update({"name" : "cd1"}, 
                        {
                            "$push" : 
                            {
                                "artists" : {"name" : "Kurt Cobain"}
                            }, 
                            "$inc": {"nbArtists" : 1}
                        })

        self.assertEqual(self.cds.find({"name" : "cd1", "artists.name" : "Kurt Cobain", "nbArtists" : 1}).count(), 1)


     #  Ce test permet de vérifier que nous pouvons mettre a jour plusieurs CD d'un coup en ajoutant une note par défaut de 0 (rating)
    def testUpdateMulti(self):

        self.testBatchInsert()

        self.cds.update({}, {"$set" : {"rating" : 0}}, multi=True)

        self.assertEqual(self.cds.find({"rating" : 0}).count(), 2)

     #  Ce test permet de vérifier l'ajout de tag. Un tag ne peut être en double
    def testAddTag(self):

        self.testInsertWorks()

        self.cds.update({}, {
                                "$addToSet" : 
                                {   
                                    "tags" : 
                                    {
                                        "$each" : ['grunge', 'funk', 'soul', 'grunge']
                                    }
                                }
                            })

        cd = self.cds.find_one()
        self.assertEqual(len(cd['tags']), 3)

     #  Ce test permet de vérifier la suppression de tag.
    def testRemoveTag(self):

        self.testAddTag()

        self.cds.update({}, {"$pullAll" : {"tags" : ['grunge', 'funk']}})

        cd = self.cds.find_one()
        self.assertEqual(len(cd['tags']), 1)


     #  Ce test permet de vérifier la suppression de tag.
    def testAddSortedRatingAndLimitBy3(self):

        self.testInsertWorks()

        self.cds.update({}, {"$push" : 
            {
                "ratings" : 
                {
                    "$each" :
                    [
                        {"rating" : 1, "date" : datetime(2010, 01, 15, 00, 00)},
                        {"rating" : 4, "date" : datetime(2011, 01, 15, 00, 00)},
                        {"rating" : 2, "date" : datetime(2009, 01, 15, 00, 00)},
                        {"rating" : 5, "date" : datetime(2013, 01, 15, 00, 00)}
                    ],
                    "$sort" : {"date" : 1}, 
                    "$slice" : -3
                }
            }})


        cd = self.cds.find_one()
        print cd
        self.assertEqual(len(cd['ratings']), 3)   
        self.assertEqual(cd['ratings'][2]['rating'], 5)  
        self.assertEqual(cd['ratings'][0]['rating'], 1)       

if __name__ == '__main__':
    unittest.main()



