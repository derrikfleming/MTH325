test1 = ("A","B")
test2 = ("A","B","C")
"""
Creates a power set from the list
"""
def power(inlist):
    #performs a bitwise opperation
  return [[inlist[j] for j in range(len(inlist))
   if (i&(1<<j))] for i in range(1<<len(inlist))]


#print (power(test2))

def partite_sets(graph):
    left = []
    right =[]
    #adds the first vertex to the left list
    for a in graph:
        left+= a
        break
    for x in graph:
        #checks vertices x is connected to and adds them to the right list
        if x in left:
            for y in graph[x]:
                if y not in right:
                    right += y
        else:
            #if x insnt in the left list it adds x's connected vertices to the
            #the left list meaning x is in the right
            for i in graph[x]:
                if i not in left:
                    left += i

    final = []
    final.append(left)
    final.append(right)

    return final



#print (partite_sets({"A" : ["B", "C"], "B" : ["A","C"], "C" : ["A","B"]}))
#print (partite_sets({"A": ["E","C"] , "B":["E","C"], "C": ["B","A"], "D":["E"], "E":["D","B","A"]}))


def is_perfect(graph):
    #calls partite set on graph and set graphT to that graph
    graphT = partite_sets(graph)
    left = graphT[0]
    right = graphT[1]
    result = True


    for a in graph:
        if a in left:
            #if a vertex a is connected to is not in the right its not perfect
            if graph[a] != right:
                result = False
        else:
            #or if its not in the left
            if graph[a] != left:
                result = False

    return result


#print (is_perfect(({"A" : ["B", "C"], "B" : ["A","D"], "C" : ["A", "D"], "D" : ["B","C"]})))

def is_bipartite(graph):
    #calls partite set on graph and set graphT to that graph
    graphT = partite_sets(graph)
    left = graphT[0]
    right = graphT[1]
    result = True

    for a in left:
        #if a is in the right and the left its not a bipartite
        if a in right:
            result = False

    return result

#print (is_bipartite({"A" : ["B", "C"], "B" : ["A"], "C" : ["A"]}))
