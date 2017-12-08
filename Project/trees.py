from copy import deepcopy

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
            A dictionary with a list of lists that contain a vertex
            (string) and a edge weight (int)

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

def is_cycle(temp_graph, original, current, prev, visited):
    """
        A recursive solution to identifying cycles where a temporary
        graph is passed in, a starting point, the current vertex being
        examined, the previous vertex examined, and a list of vertexes
        on the current path. At each recursive iteration it checks to
        make sure that the current vertex is not being mapped back onto
        the original.

        Parameters:
        --------------
        temp_graph : dictionary
        original : string
        current : string
        prev : string
        visited : string

        Returns:
        --------------
        list
    """

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

def min_kruskal(graph):
    """


        Parameters:
        --------------
        graph : dictionary


        Returns:
        --------------
        list

    """

    kruskal_mst = []
    temp_graph = {}
    temp_graph2 = {}

    #init temp dicts with key values
    for g in graph:
        temp_graph[g] = []
        temp_graph2[g] = []
    #get edges in graph
    kruskal_g = edge_get(graph)

    for edge in kruskal_g:
        temp_graph2[edge[0]] += edge[1]
        temp_graph2[edge[1]] += edge[0]
        if is_cycle(temp_graph2,edge[0],edge[0],edge[0],[]) == False:
            temp_graph = deepcopy(temp_graph2)
            kruskal_mst.append(edge)
        else:
            temp_graph2 = deepcopy(temp_graph)
    return kruskal_mst


def min_prim(graph):
    """
        Due to the length of this method, please refer to inline
        comments.

        Parameters:
        --------------
        graph : dictionary

        Returns:
        --------------
        list

    """

    prims_g= edge_get(graph)
    mst = []
    temp_graph = {}
    temp_graph2 = {}
    # initialize temps to hold empty lists []
    for g in graph:
        temp_graph[g] = []
        temp_graph2[g] = []
    # add the first edge to the mst and temp graphs
    mst.append(prims_g[0])
    temp_graph2[prims_g[0][0]] += prims_g[0][1]
    temp_graph2[prims_g[0][1]] += prims_g[0][0]
    temp_graph = deepcopy(temp_graph2)
    # remove first edge from edgelist
    prims_g.pop(0)
    # delete edges in prims_g if added to mst until either there is nothing left or
    # the only edges we can add create cycles
    while(len(mst) < len(graph.keys())-1):
        check = False
        # loop through the edges to find the next one to add
        for edge in prims_g:
            # loop through mst to see if the current edge to add contains a vertex currently in the mst
            for x in mst:
                # if there is an edge that has a vertex part of the current mst add it to the temp and make sure it doesnt create a cycle
                if edge[0] in x or edge[1] in x:
                    temp_graph2[edge[0]] += edge[1]
                    temp_graph2[edge[1]] += edge[0]
                    # if no cycle is made, commit it to the other temp and add that edge to mst and remove it from the edgelist
                    if is_cycle(temp_graph2, edge[0], edge[0], edge[0], []) == False:
                        temp_graph = deepcopy(temp_graph2)
                        mst.append(edge)
                        prims_g.remove(edge)
                        check = True
                        break
                    # if it does make a cycle, undo that edge
                    else:
                        check = False
                        temp_graph2 = deepcopy(temp_graph)
            if check == True:
                break
    return mst
