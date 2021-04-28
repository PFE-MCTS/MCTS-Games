from Node import *
from Game import *
from MCTS import *
import numpy as np


root=Nodes(None,None,"0,0")

child1=Nodes(None,root,"1,2")
child2=Nodes(None,root,"1,1")
child4=Nodes(None,child1,"0,1")
child3=Nodes(None,child2,"2,2")

root.children.append(child1)
root.children.append(child2)
child2.children.append(child3)
child2.children.append(child4)

mcts=Mcts(Game, root, 0)

mcts.select_leaf(root)
print(mcts.LeafList[0].value)
game = Game()
'''
mcts.expand_Node(game, child4)

print(child4.__dict__)
'''


'''print(root.children)
print(child2.children)
'''




