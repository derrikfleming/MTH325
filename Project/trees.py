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
    if len(level) > 0:
        bfs_list += level
        sub_level = []
        for vertex in level:
            sub_level += tree[vertex]
        bfs_list += BFS(tree,sub_level)
    return bfs_list


#            ___A___
#           /       \
#          C         D
#        / | \     / | \
#       P  R  L   F  Q  S
#         / \       / \
#        O   E     G   H
#                 / \
#                N   M
#
#tree = {"A" : ["C", "D"], "C" : ["P","R","L"],"R" : ["O","E"],"P" : [], "L" : [], "N" : [], "M" : [], "H" : [], "S" : [], "F" : [], "O" : [], "E": [], "G" : ["N", "M"], "Q" : ["G", "H"], "D" : ["F", "Q", "S"]}
#print(BFS(tree))
#A,C,D,P,R,L,F,Q,S,O,E,G,H,N,M

#from isomorphisms
def is_same(list1, list2):
    is_same = True

    if len(list1) == len(list2):
        for item in list1:
            if item not in list2:
                is_same = False
    else:
        is_same = False
    return is_same

def edge_get(graph):
    edge_list = []
    weights = []

    for node in graph:
        for adj_edge in graph[node]:
            #the current edge
            curr_edge = [node, adj_edge[0]]
            #edge_list empty, ie first iteration
            if len(edge_list) < 1:
                edge_list.append(curr_edge)
                weights.append(adj_edge[1])
            else:
                in_list = False
                #check edge_list for curr_edge's existance
                for i in edge_list:
                    if is_same(i,curr_edge):
                        in_list = True
                        break
                if not in_list:
                    #sort edge_list while building
                    for i in range(len(edge_list)):
                        if weights[i] >= adj_edge[1]:
                            edge_list.insert(i,curr_edge)
                            weights.insert(i,adj_edge[1])
                            break
                        if i == len(edge_list)-1:
                            edge_list.append(curr_edge)
                            weights.append(adj_edge[1])
    return edge_list

#
#           A
#      10  / \  5
#         B   D
#     5  /___/  15
#       C
#
#
#tree = {"A" : [["B", 10], ["D", 5]], "B" : [["A", 10], ["C",5]], "C" : [["B", 5], ["D", 15]], "D" : [["C", 15], ["A", 5]]}
#print(edge_get(tree))
def is_cycle(temp_graph,vertex):
    is_cycle = False
    temp = {}
    temp = temp_graph
    for stuff in temp_graph{vertex}:



    return is_cycle

def min_kruskal(graph):
    kruskal_mst = []
    temp_graph = {}
    kruskel_g = edge_get(graph)
    for edge in kruskel_g:
        if !is_cycle(temp_graph, edge):
            temp_graph[edge[0]] += edge[1]
            temp_graph[edge[1]] += edge[0]
            kruskal_mst.append(edge)
    return kruskal_mst

def min_prim(graph):
    prim_mst = []
    edge_list = edge_get(graph)

    edge_to_add = []
    for edge in edge_list:
        if "A" in edge:
             edge_to_add = edge
             break

    if len(prim_mst) < 2:


    return prim_mst

tree = {"A":[["B", 10], ["D",5]], "B":[["A",10], ["C",5]], "C":[["B",5], ["D",15]], "D":[["C",15], ["A",5]]}
