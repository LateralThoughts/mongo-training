# -*- coding: utf-8 -*-
import unittest
import pymongo
from datetime import datetime
from pymongo import MongoClient


class MongoWriteTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = None
        self.db = None
        self.cds = None

    def tearDown(self): 
        # A completer
        self.mongoclient.close()

    
    """
    Ce test d'exemple permet de vérifier que nous avons bien 0 CDs en base de données
    La collection est vide, c'est normal car nous allons la remplir dans les tests suivants
    """
    @unittest.skip('Remove to play this test')
    def testThatDatabaseHas0Cds(self):
        self.assertEqual(self.cds.find().count(), 0)        

    """
    Ce test permet de vérifier qu'une insertion est prise en compte
    """
    @unittest.skip('Remove to play this test')
    def testInsertWorks(self):
        cd = {"name" : "cd1"}

        # TODO

        self.assertEqual(self.cds.find().count(), 1)                

    """
    Ce test permet de vérifier qu'une insertion par batch est prise en compte
    """
    @unittest.skip('Remove to play this test')
    def testBatchInsert(self):
        cd1 = {"name" : "cd1"}
        cd2 = {"name" : "cd2"}

        # TODO

        self.assertEqual(self.cds.find().count(), 2)   

    """
    Ce test permet de vérifier que nous pouvons mettre à jour le nom du CD
    """
    @unittest.skip('Remove to play this test')
    def testUpdateName(self):

        self.testInsertWorks()

        # TODO

        self.assertEqual(self.cds.find({"name" : "cd1"}).count(), 0)
        self.assertEqual(self.cds.find({"name" : "new name"}).count(), 1)

    """
    Ce test permet de vérifier que nous pouvons ajouter un artiste 
    sur le CD et incrémenter un compteur nbArtiste par la même occasion
    """
    @unittest.skip('Remove to play this test')
    def testUpdateAndIncr(self):

        self.testInsertWorks()

        # TODO

        self.assertEqual(self.cds.find({"name" : "cd1", "artists.name" : "Kurt Cobain", "nbArtists" : 1}).count(), 1)


    """
    Ce test permet de vérifier que nous pouvons mettre a jour plusieurs CD 
    d'un coup en ajoutant une note par défaut de 0 (rating)
    """
    @unittest.skip('Remove to play this test')
    def testUpdateMulti(self):

        self.testBatchInsert()

        # TODO

        self.assertEqual(self.cds.find({"rating" : 0}).count(), 2)

    """
    Ce test permet de vérifier l'ajout de tag. Un tag ne peut être en double
    """
    @unittest.skip('Remove to play this test')
    def testAddTag(self):

        self.testInsertWorks()

        tagsToAdd = ['grunge', 'funk', 'soul', 'grunge']

        # TODO

        cd = self.cds.find_one()
        self.assertEqual(len(cd['tags']), 3)

    """
    Ce test permet de vérifier la suppression de tag.
    """
    @unittest.skip('Remove to play this test')
    def testRemoveTag(self):

        self.testAddTag()

        tagsToRemove = ['grunge', 'funk']

        # TODO

        cd = self.cds.find_one()
        self.assertEqual(len(cd['tags']), 1)


    """
    Dans ce test, nous allons mettre à jour un enregistrement pour lui insérer 4 nouvelles notes
    Mais sur ces 4 notes, nous n'allons en conserver que 3, les 3 plus récentes
    """
    @unittest.skip('Remove to play this test')
    def testAddSortedRatingAndLimitBy3(self):

        self.testInsertWorks()

        ratings = [
                        {"rating" : 1, "date" : datetime(2010, 01, 15, 00, 00)},
                        {"rating" : 4, "date" : datetime(2011, 01, 15, 00, 00)},
                        {"rating" : 2, "date" : datetime(2009, 01, 15, 00, 00)},
                        {"rating" : 5, "date" : datetime(2013, 01, 15, 00, 00)}
                    ]

        # TODO


        cd = self.cds.find_one()
        print cd
        self.assertEqual(len(cd['ratings']), 3)   
        self.assertEqual(cd['ratings'][2]['rating'], 5)  
        self.assertEqual(cd['ratings'][0]['rating'], 1)       

if __name__ == '__main__':
    unittest.main()



