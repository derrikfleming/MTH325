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
    dfs_list = []
    if vertex not in dfs_list:
        dfs_list += vertex
        for child in tree[vertex]:
            dfs_list += DFS(tree,child)
    return dfs_list


print(DFS(tree))
#A,B,E,F,I,J,K,C,G,D,H
