# -*- coding: utf-8 -*-
import unittest
import pymongo
from pymongo import MongoClient
import re


class MongoIndexTest(unittest.TestCase):

    #
    # Initialisation des membres privés à compléter
    def setUp(self):
        self.mongoclient = MongoClient()


    def tearDown(self): 
        self.mongoclient.close()


    """
    Il ne s'agit pas d'un test unitaire

    Chaque requête utilise un critère de filtre et parcoure la liste des résultats.
    Vous devez lancer ce test de la façon habituelle et faire en sorte de diminuer le temps d'execution total
    """
    @unittest.skip('Remove to play this test')
    def testThatIndexesAreOk(self):
        
        messages = self.mongoclient.enron.messages;

        regx = re.compile("ROOM", re.IGNORECASE)

        listOfMessages = messages.find({"body": regx})
        for message in listOfMessages:
            pass

        listOfMessages = messages.find({"headers.X-From": "Reservations@Marriott.com", "headers.X-To" : "EBASS@ENRON.COM"})
        for message in listOfMessages:
            pass    

        listOfMessages = messages.find({'mailbox' : "sent", "headers.X-cc" : ""}).sort([('headers.From',1)])
        for message in listOfMessages:
            pass    

        listOfMessages = messages.find({'headers.From' : "eric.bass@enron.com"}).sort([('headers.Date',-1)])
        for message in listOfMessages:
            pass   
        



if __name__ == '__main__':
    unittest.main()
