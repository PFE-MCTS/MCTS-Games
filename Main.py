from Node import *
from Game import *
import numpy as np


root=Nodes(None,None)
root.add_children(game=Game())
print(root.children[0].moves)

A=np.array([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]])

