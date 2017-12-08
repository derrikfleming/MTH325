def is_same(list1, list2):
    """

    """

    is_same = True

    if len(list1) == len(list2):
        for item in list1:
            if item not in list2:
                is_same = False
            else:
                list2.remove(item)

    else:
        is_same = False
    return is_same

def switch(graph,vert1,vert2):
    """
    
    """
    temp_g = graph

    for x in list(temp_g):
        for y in temp_g[x]:
            # checks if the edge connected to the vertex x is what vert2 is
            #if it is it removes it after getting its index and then adds vert1
            #at that index
            if y == vert2:
                ind = temp_g[x].index(vert2)
                temp_g[x].remove(vert2)
                temp_g[x].insert(ind,vert1)
            elif y == vert1:
                ind = temp_g[x].index(vert1)
                temp_g[x].remove(vert1)
                temp_g[x].insert(ind,vert2)

    x1 = temp_g[vert1]
    x2 = temp_g[vert2]
    #checks to see if that key is vert1 or vert2 and swaps the vertex
    for i in temp_g:
        if i == vert1:
            temp_g[vert2] = x1
        elif i == vert2:
            temp_g[vert1] = x2

    return temp_g


#print (switch({"A" : ["B", "C"], "B" : ["A", "D"], "C" : ["A", "D"], "D" : ["B", "C"]}, "A", "C"))

g = []
def list_perm(list,step = 0):
    """
    Method that finds all permutations for the given list.
    """
    #adds each permutation to g
    if step == len(list):
        global g
        g +=([list])

    for i in range(step, len(list)):
        lst_temp= [character for character in list]
        lst_temp[step], lst_temp[i] = lst_temp[i], lst_temp[step]
        #recurses back through perm for the next character in the list.
        list_perm(lst_temp, step + 1)
    else:
        return g

#print(list_perm(["A","B","C"]))

def is_iso(graph1,graph2):
    """

        Parameters:
        --------------
        graph1 : dictionary
        graph2 : dictionary

        Returns:
        --------------
        boolean
            True if isomorphic, False if not
    """

    temp_g1 = []
    g1 = {}
    g1 = graph1
    result = True

    if len(graph1.keys()) != len(graph2.keys()):
        result = False
    else:
        degrees_g1 = []
        degrees_g2 = []
        for v1,v2 in zip(graph1,graph2):
            degrees_g1.append(len(graph1[v1]))
            degrees_g2.append(len(graph2[v2]))
        print(degrees_g1, degrees_g2)
        result = is_same(degrees_g1,degrees_g2)

    return result
