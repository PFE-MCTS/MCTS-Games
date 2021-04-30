from Node import *
from Game import *
from MCTS import *
import numpy as np


root=Nodes(None,None,0)

child1=Nodes(None,root,1)
child2=Nodes(None,root,2)
child4=Nodes(None,child1,3)
child3=Nodes(None,child2,4)

root.children.append(child1)
root.children.append(child2)
child2.children.append(child3)
child2.children.append(child4)

mcts=Mcts(Game, root, 0)

print(mcts.get_ActualState(child4))

'''partie= Game()
partie.play()
'''


'''mcts.BackPropagation(child4, partie)

print("Game.Score=", partie.Score)
print("Child 1 score= ",child1.Score)
print("child1 Visits=",child1.Visits)

print(" root Score ", root.Score)

print("root visites ", root.Visits)

mcts.select_leaf(root)
print(mcts.LeafList[0].value)
game = Game()'''

'''
mcts.expand_Node(game, child4)

print(child4.__dict__)
'''


'''print(root.children)
print(child2.children)
'''




