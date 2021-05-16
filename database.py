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

def deleteTree(data):                                           # suppression de l'arbre precedent
    collection = data['tree']
    collection.delete_many({})

def updateTreesearch(database,root:TNode):
    '''
    fonction qui met a jour l'arbre de recherche dans la base de donnée apres la fin d'une partie
    '''
                # création d'un nouvel arbre

    if (root.parent == None):
        # Ajout de la racine
        database.tree.insert_one(
            {
                "_id": root.id,
                "parent": None,
                "children": [],
                "visits": root.Visits,
                "score": root.Score,
                " value": root.value,
                "gameState": root.currentGameState
            }
        )

    if root.children != []:
        for node in root.children:
            database.tree.insert_one(
                {
                    "_id": node.id,
                    "parent": root.id,
                    "children": [],
                    "visits": node.Visits,
                    "score": node.Score,
                    " value": node.value,
                    "gameState": node.currentGameState
                }
            )
                        # on ajoute le fils chez le pére
            database.tree.update_one({'_id': root.id}, {'$push': {'children': node.id}})
                        # appel recurssif
            updateTreesearch(database, node)




currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer' : "X", 'value': None}
'''
root= TNode(None,currentGameState)
child1= TNode(root,currentGameState,1)
child2= TNode(root,currentGameState,2)
child3= TNode(root,currentGameState,3)
child4= TNode(child1,currentGameState,4)
child5= TNode(child2,currentGameState,5)
child6= TNode(child3,currentGameState,6)
child7=TNode(child1,currentGameState,7)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)
child1.children.append(child7)
child1.children.append(child4)
child2.children.append(child5)
child3.children.append(child6)



database = connection("tictactoe")
deleteTree(database)
updateTreesearch(database,root)
'''























