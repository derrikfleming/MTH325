#           A
#         / | \
#        B  C  D
#      / |  |   \
#     E  F  G    H
#      / | \
#     I  J  K
#

tree = {"A":["B", "C", "D"],"B":["E","F"], "C" : ["G"], "D" : ["H"], "E" : [], "F" : ["I","J","K"], "G" : [], "H" : [], "I" : [], "J" : [], "K" : []}

def DFS(tree,vertex="A"):
    visited = []
    if vertex not in visited:
        visited += vertex
        for v in tree[vertex]:
            visited += DFS(tree,v)
    return visited


print(DFS(tree))
#A,B,E,F,I,J,K,C,G,D,H
