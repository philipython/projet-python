"""on execute tout dans le main
ctrl + clic + run in interractive window : donne les resultats dans une nouvelle fenetre
"""

from grid import Grid
from graph import Graph

# test is_sorted
print("test is_sorted : ")
grille_init1 = [[1,3],[4,2]]
nouvelle_grille1 = Grid(len(grille_init1),len(grille_init1[0]), grille_init1)
print(nouvelle_grille1)

result = nouvelle_grille1.is_sorted()
print("Is grid sorted?", result)

grille_init2 = [[1,2],[3,4]]
nouvelle_grille2 = Grid(len(grille_init2),len(grille_init2[0]), grille_init2)
print(nouvelle_grille2)

result = nouvelle_grille2.is_sorted()
print("Is grid sorted?", result)


# test swap
print("test swap : ")
grille_init1 = [[1,3],[4,2]]
nouvelle_grille1 = Grid(len(grille_init1),len(grille_init1[0]), grille_init1)
print(nouvelle_grille1)

un_swap = nouvelle_grille1.swap((1,0), (1,1))
print(un_swap)

# test swap
print("test swap_seq : ")
grille_init1 = [[1,3],[4,2]]
nouvelle_grille1 = Grid(len(grille_init1),len(grille_init1[0]), grille_init1)
print(nouvelle_grille1)

plsr_swap = nouvelle_grille1.swap_seq([((0,1), (1,1)),((1,0),(1,1))])
print(plsr_swap)

# test trace
print("test trace pour la représentation graphique")
grille_init1 = [[1,3],[4,2]]
nouvelle_grille1 = Grid(len(grille_init1),len(grille_init1[0]), grille_init1)
print(nouvelle_grille1)

representation = nouvelle_grille1.trace()
print(representation)

# test make_hashable
print("test make_hashable")
grille_init1 = [[1,3],[4,2]]
nouvelle_grille1 = Grid(len(grille_init1),len(grille_init1[0]), grille_init1)

tup = nouvelle_grille1.make_hashable()
print(tup)

# test grids_graph
print("test grids_graph")
grille_init1 = [[1,3],[4,2]]
nouvelle_grille1 = Grid(len(grille_init1),len(grille_init1[0]), grille_init1)

arrangements = nouvelle_grille1.grids_graph()
print(arrangements)

# test all_edges
print("test all_edges")
grille_init1 = [[1,3],[4,2]]
nouvelle_grille1 = Grid(len(grille_init1),len(grille_init1[0]), grille_init1)

noeuds = nouvelle_grille1.all_edges()
print(noeuds)












data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g2 = Grid.grid_from_file(file_name)



from graph import Graph
graph = Graph()
graph.add_edge("Paris","Palaiseau")




grille_init = [[1,3],[4,2]]

