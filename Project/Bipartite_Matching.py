test1 = ("A","B")
test2 = ("A","B","C")

def power(inlist):

  return [[inlist[j] for j in range(len(inlist))
   if (i&(1<<j))] for i in range(1<<len(inlist))]


#print (power(test2))

def partite_sets(graph):
    left = []
    right =[]
    for a in graph:
        left+= a
        break
    for x in graph:
        if x in left:
            for y in graph[x]:
                if y not in right:
                    right += y
        else:
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
    graphT = partite_sets(graph)
    left = graphT[0]
    right = graphT[1]
    result = True

    for a in graph:
        if a in left:
            if graph[a] != right:
                result = False
        else:
            if graph[a] != left:
                result = False

    return result


#print (is_perfect(({"A" : ["B", "C"], "B" : ["A","D"], "C" : ["A", "D"], "D" : ["B", "C"]})))

def is_bipartite(graph):
    graphT = partite_sets(graph)
    left = graphT[0]
    right = graphT[1]
    result = True

    for a in left:
        if a in right:
            result = False

    return result

print (is_bipartite({"A" : ["B", "C"], "B" : ["A"], "C" : ["A"]}))
