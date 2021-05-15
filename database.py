from copy import deepcopy
import pymongo
from pymongo import MongoClient
from Node import *

client = MongoClient()

'''
        self.parent = parent
        self.children = []
        self.Visits = 0
        self.Score = 0
        self.value = value
        self.currentGameState = GameState


        
                              " ", "O", "O",
                              " ", " ", " "],
                     nextPlayer: "O", 'value':'1'
                }
        
'''

def connection(database, localhost="localhost", port=27017):
    client = MongoClient(host=localhost, port=port)
    db = client[database]
    return db
    print("connected successfuly to the database:", client)


def getTreesearch():
    '''
        fonction qui charge en memoire l'arbre de recherche d'un jeu  sous forme d'objets

    :return: la racine de l'arbre ou False si l'arbre n'existe pas
    '''
    pass

def updateTreesearch(database, root:TNode):
    '''
    fonction qui met a jour l'arbre de recherche dans la base de donnée apres la fin d'une partie
    '''
                # suppression de l'arbre precedent
    data = connection(database)
    collection = data['tree']
    collection.delete_many({})
                # création d'un nouvel arbre

                # Ajout de la racine
    database.tree.insert_one(
        {
            "_id": "root",
            "parent": None,
            "children": [],
            "visits": root.Visits,
            "score": root.Score,
            " value": root.value,
            "gameState": root.currentGameState
        }
    )
    rootID = "root"
    if root.children !=[]:
        for node in root.children:
            database.tree.insert_one(
                {
                    "parent": rootID,
                    "children": [],
                    "visits": node.Visits,
                    "score": node.Score,
                    " value": node.value,
                    "gameState": node.currentGameState
                }
            )

























