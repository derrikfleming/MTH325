def DFS(tree,vertex="A"):
    """
    This method provides a recursive DFS traversal of the tree
    parameter passed in. It maintains a list of each parent and
    child vertice which is returned to each parent via the
    recursive call.

        Parameters:
        --------------
        tree : dictionary
            The tree parameter is a dictionary with each key having a
            value of its child vertices associated with it
        vertex : string
            The vertex parameter hold the current parent relative to
            the recursive call. It is "A" by default as that is the
            specified starting point per Prof Santana

        Returns:
        --------------
        list
            A list of strings representing each vertex in DFS order.
    """
    dfs_list = []

    #if vertex has not been visited
    if vertex not in dfs_list:
        dfs_list += vertex

        #for each child of the vertex
        for child in tree[vertex]:
            dfs_list += DFS(tree,child)

    return dfs_list

# A TEST CASE
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
    """
    This method provides a BFS traversal of the tree parameter
    passed in. It maintains a list of strings representative of
    each vertex in the tree. For each "level" of the tree it makes
    a recursive call passing in each vertex contained within the
    "sub-level", (or a list of all of the children of each vertex
    in "level").

        Parameters:
        --------------
        tree : dictionary
            The tree parameter is a dictionary with each key having a
            value of its child vertices associated with it
        level : list
            The level parameter is a list of strings representative of
            each vertex in a specific "level" of the tree

        Returns:
        --------------
        list
            A list of strings representative of the each vertex of the
            tree traversed in BFS order
    """

    bfs_list = []

    if len(level) > 0:
        bfs_list += level
        sub_level = []
        for vertex in level:
            sub_level += tree[vertex]
        bfs_list += BFS(tree,sub_level)
    return bfs_list

# A TEST CASE
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
    """
    This method returns a list of lists representative of vertex pairs
    (strings) in non-decreasing order. For each key in the dictionary,
    every value is evaluated. If the pair (key,value) already appears
    in edge_list it is ignored, if not it is inserted by comparing it's
    edge weight with the others contained in the list via weights[].

        Parameters:
        --------------
        graph : dictionary
            A dictionary with a list of lists that contain a vertex (string) and a edge weight (int)

        Returns:
        --------------
        list
            A list of strings representative of the each vertex of the
            tree traversed in BFS order
    """
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

#NOT WORKING!
# def is_cycle(temp_graph,original_vertex, current, prev):
#     cycle = False
#     for edge in temp_graph:
#         if edge == current:
#             for vertex in edge:
#                 if vertex == original_vertex and vertex != prev:
#                     print ("cycle")
#                     return True
#                 else:
#                     cycle = cycle or is_cycle(temp_graph, original_vertex, vertex, edge)
#     return cycle

def is_cycle(temp_graph, original, current, prev, visited):
    result = False

    if len(temp_graph[current]) == 1:
        result = False
    else:
        visited.append(current)
        for x in temp_graph[current]:
            if x == original and x != prev:
                result = True
            else:
                if x not in visited:
                    result = is_cycle(temp_graph, original, x, current, visited)
            if result is True:
                break
    return result


print(is_cycle({"A":["B","D"], "B":["A","C"], "C":["B","D"],"D":["C", "L"], "L":["D","A"]}, "A", "A", "A",[]))

from copy import deepcopy
def min_kruskal(graph):
    kruskal_mst = []
    temp_graph = {}
    temp_graph2 = {}
    kruskel_g = edge_get(graph)
    for edge in kruskel_g:
        e1 = edge[1]
        e0 = edge[0]
        temp_graph2[e0].append(e1)
        temp_graph2[e1].append(e0)
        if is_cycle(temp_graph2, edge[0], edge[0], edge[0], []) == False:
            temp_graph = deepcopy(edge)
            kruskal_mst.append(edge)
        else:
            temp_graph2 = deepcopy(temp_graph)
    return kruskal_mst

# def min_prim(graph):
#     prim_mst = []
#     edge_list = edge_get(graph)
#
#     edge_to_add = []
#     for edge in edge_list:
#         if "A" in edge:
#              edge_to_add = edge
#              break
#
#     if len(prim_mst) < 2:
#
#
#     return prim_mst

tree = {"A":[["B", 10], ["D",5]], "B":[["A",10], ["C",5]], "C":[["B",5], ["D",15]], "D":[["C",15], ["A",5]]}
print(min_kruskal(tree))
