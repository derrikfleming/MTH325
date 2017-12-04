def DFS(tree,vertex="A"):
    dfs_list = []

    #if vertex has not been visited
    if vertex not in dfs_list:
        dfs_list += vertex

        #for each child of the vertex
        for child in tree[vertex]:
            dfs_list += DFS(tree,child)

    return dfs_list

#           A
#         / | \
#        B  C  D
#      / |  |   \
#     E  F  G    H
#      / | \
#     I  J  K
#

#tree = {"A":["B", "C", "D"],"B":["E","F"], "C" : ["G"], "D" : ["H"], "E" : [], "F" : ["I","J","K"], "G" : [], "H" : [], "I" : [], "J" : [], "K" : []}
#print(DFS(tree))
#A,B,E,F,I,J,K,C,G,D,H

def BFS(tree,level=["A"]):
    bfs_list = []
    sub_level = []
    if len(level) > 0:
        bfs_list += level
        for vertex in level:
            sub_level += tree[vertex]
        bfs_list += BFS(tree,sub_level)
    return bfs_list

tree = {"A":["C", "D"], "C" : ["P","R","L"],"R" : ["O","E"],"P" : [], "L" : [], "N" : [], "M" : [], "H" : [], "S" : [], "F" : [], "O" : [], "E": [], "G" : ["N", "M"], "Q" : ["G", "H"], "D" : ["F", "Q", "S"]}
print(BFS(tree))
#
