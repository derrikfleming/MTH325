def is_proper(graph,color):
	for vert in graph:
		for adj in graph[vert]:
			if color[adj] == color[vert]:
				return False
	return True

def three_color(graph):
	print (len(graph))
	temp = []
	tempa = []
	for x in range(len(graph)):
		temp.append([1,2,3])
	print (temp[1])
	tempa = [[x,y,z] for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]
	print(tempa)

if __name__ == "__main__":
	graphEmpty = {}
	grapha = {"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B"]}
	colora = {"A" : 1, "B" : 2, "C" : 3}
	colorb = {"A" : 1, "B" : 1, "C" : 3}
	boola = is_proper(grapha, colora)
	boolb = is_proper(grapha, colorb)
	print (boola, boolb)
	graphb = {"A":["B"],"B":["A"]}
	three_color(graphb)


	f = graphb["A"][0]
	final = []
	final.append({f:1})
	#print (final)
	#print([(x, y, z) for x in [1,2,3] for y in [1,2,3] for z in [1,2,3] ])
