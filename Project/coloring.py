"""
This method determines if a graph has a vertex proper coloring.
"""
def is_proper(graph,color):
	# loops through all the vertices connected to each vertex and checks
	# if they have the same color, returns false if so
	for vert in graph:
		for adj in graph[vert]:
			if color[adj] == color[vert]:
				return False
	return True

"""
This method returns all possible vertex colorings of a graph. Does not distinguish
between proper and non-proper colorings.
"""
def three_color(graph):
	temp = {}
	final = []
	# sets every vertex to color 1
	for vert in graph:
		temp[vert] = 1
	final.append(dict(temp))
	# loops through the number of possible graphs (the length of the graph^3)
	for x in range(len(graph)**3):
		# loops through the vertices in temp, if it is less than 3, its adds 1
		# adds it to the final and breaks out to the next possibility
		# otherwise if it is >= 3 it sets it back to one and moves on to the next
		# vertex in the temp
		for vert in temp:
			if temp[vert] < 3:
				temp[vert] += 1
				final.append(dict(temp))
				break
			else:
				temp[vert] = 1
	return final

"""
This method determines if the inputed graph's vertices can be colored with only
three colors.
"""
def is_three_color(graph):
	# runs the three_color method to retrieve all the possible vertex colorings
	# of a graph using only three colors
	combinations = three_color(graph)
	# loops through possibly colorings and checks if it is_proper and returns
	# true if it finds one that works
	for poss in combinations:
		if is_proper(graph,poss):
			return True
	return False

"""
This method determines if a graph has a proper edge coloring>
"""
def is_proper_edge(graph):
	# loops through all the edges and its neighboring edges and checks
	# if they have the same color, returns false if so
	for vert in graph:
		for edge in graph[vert]:
			for l in graph[edge[0]]:
				if l[0] != vert and l[1] == edge[1]:
					return False
	return True

"""
This method performs the greedy algorithm to find the a proper vertex coloring
of a graph given an order.
"""
def greedy(graph,order):
	color = {}
	# sets the first vertex to have color 1 otherwise the following loops would
	# fail if color starts off empty
	color[order[0]] = 1
	# loops through the oder and adds it to the color dict with a color of 1
	for vert in order:
		color[vert] = 1
		# goes through the adjacent vertices that have already been colored and
		# adds their color to a list, then while the current color is the same
		# as any of the neighboring vertices it increments it up one
		neighborColors = []
		for neighbor in graph[vert]:
			if neighbor in color:
				neighborColors.append(color[neighbor])
		while(color[vert] in neighborColors):
			color[vert] += 1
	return color
