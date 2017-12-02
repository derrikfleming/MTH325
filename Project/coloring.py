def is_proper(graph,color):
	for vert in graph:
		for adj in graph[vert]:
			if color[adj] == color[vert]:
				return False
	return True

def three_color(graph):
	temp = {}
	final = []
	for vert in graph:
		temp[vert] = 1
	final.append(dict(temp))
	for x in range(len(graph)**3):
		for edge in temp:
			if temp[edge] < 3:
				temp[edge] += 1
				final.append(dict(temp))
				break
			else:
				temp[edge] = 1
	return final

def is_three_color(graph):
	combinations = three_color(graph)
	for poss in combinations:
		if is_proper(graph,poss):
			return True
	else: return False

def is_proper_edge(graph):
	return

if __name__ == "__main__":
	graphEmpty = {}
	grapha = {"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B"]}
	colora = {"A" : 1, "B" : 2, "C" : 3}
	colorb = {"A" : 1, "B" : 1, "C" : 3}
	boola = is_proper(grapha, colora)
	boolb = is_proper(grapha, colorb)
	print (boola, boolb)
	graphb = {"A":["B"],"B":["C"],"C":["A"]}
	print(three_color(graphb))
	graphc = {"A":["B"],"B":["C"],"C":["A"], "D":["A","B","C"]}
	print(is_three_color(graphc))

	g = {"A" : [["B", 1], ["C", 2]], "B" : [["A", 1], ["C", 3]],"C" : [["A", 2], ["B", 3]]}

	for x in g:
		print (x)
		print (g[x])
		print (g[x][1][1])
