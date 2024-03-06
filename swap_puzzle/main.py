"""on execute tout dans le main
ctrl + clic + run in interractive window : donne les resultats dans une nouvelle fenetre
"""

from grid import Grid

g1 = Grid(2, 3)


data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g2 = Grid.grid_from_file(file_name)



from graph import Graph
graph = Graph()
graph.add_edge("Paris","Palaiseau")

"test is_sorted"
A = Grid

grille_init = [[1,3],[4,2]]
nouvelle_grille = Grid(len(grille_init),len(grille_init[0]), grille_init)
print(nouvelle_grille)
