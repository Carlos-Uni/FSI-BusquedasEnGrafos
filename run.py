# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
lb = search.GPSProblem('L', 'B', search.romania)
ob = search.GPSProblem('O', 'B', search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())


print("Ruta A-B por RyA: ", search.rya(ab).path())
print("Ruta A-B por RyAs: ", search.ryas(ab).path())
print()
print("Ruta L-B por RyA: ", search.rya(lb).path())
print("Ruta L-B por RyAs: ", search.ryas(lb).path())
print()
print("Ruta O-B por RyA: ", search.rya(ob).path())
print("Ruta O-B por RyAs: ", search.ryas(ob).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
