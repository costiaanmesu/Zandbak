from graphviz import *

g2 = Digraph(format='svg')
g2.node('A')
g2.node('B')
g2.edge('A', 'B')
g2.render('img/g2')
g2.view()
g2.v
print(g2)

