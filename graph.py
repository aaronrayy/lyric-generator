''' 
class for individual vertexes
    - contains value attribute that is the string itself
    - contains a weight attribute that defaults to 1
        - weight attribute if the weight of the edge connecting current vertex and previous vertex
    - contains array of vertexes pointed to by current vertex object in the graph
    - functions:
        add_edge -> adds a new vertex to the adjacency array
        increment_edge -> increments the edge connecting vertexes if there is already an edge present
        printout -> returns a string formatted to show each vertex in the adjacency array and its weight
'''


class Vertex:
    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight
        self.adj = []                   # adj array is an array of vertexes
    def add_edge(self, val, weight=1):
        new = Vertex(val, weight)
        self.adj.append(new)
    def increment_edge(self, value):
        for i in range(len(self.adj)):
            if self.adj[i].value == value:
                self.adj[i].weight += 1
    def printout(self):
        s = ""
        for el in self.adj:
            s += "[vertex]: " + el.value + "\n     [weight]: " + str(el.weight) + "\n   "
        return s

'''
create a class for the graph of vertexes
    - contains a dictionary of vertexes
        - keys: vertex.value attributes (string representing the vertex word)
    - functions:
        add_vertex -> adds a new vertex to the dictionary if not already present
        update_adj -> takes 2 vertexes and either increments their edge weight if they are already connected,
                        or if no edge exists, adds a new edge between the two vertexes
        printout -> iterates over all keys in dictionary and formats and returns a string representing each vertex and edges
'''
class Graph:
    def __init__(self):
        self.vertexes = {}
    def add_vertex(self, value, weight=1):
        if value not in self.vertexes:
            v = Vertex(value, weight)
            self.vertexes.update({v.value : v})
    def update_adj(self, i, j): # i, j are vertex objects. j is the vertex to be added to the i adjacency array
        flag = 1
        for k in range(len(i.adj)):
            if i.adj[k].value == j.value:
                i.increment_edge(j.value)
                flag = 0
        if flag==1:
            i.add_edge(j.value)  
    def printout(self):
        s = ""
        for key,val in self.vertexes.items():
            cur = self.vertexes[key]
            s += key + "\n  " + cur.printout() + "\n" 
        return s

'''
creates a populated graph given an input graph and input text file
    - inputs: 
        graph -> a graph object. Can be empty or already created
        f_in -> an input text file to graph
        f_out -> file to write the output graph to. Defaults to output.txt
'''
def populate(graph, f_in, f_out="output.txt"):
    g = graph
    f = open(f_in, 'r')
    chars = f.read()
    chars = chars.split()
    for i in range(len(chars)):
        s = ''.join(ch for ch in chars[i] if ch.isalnum())   # removing non alphanumeric chars from vertex value
        chars[i] = s
    for word in chars:
        g.add_vertex(word)
    for i in range(1, len(chars)):
        v1 = g.vertexes[chars[i-1]]
        v2 = g.vertexes[chars[i]]
        g.update_adj(v1, v2)
    fout = open(f_out, "w")
    s = g.printout()
    fout.write(s)
    f.close()
    fout.close()
    return g

'''
main routine
    - takes input text file from user 
    - creates an empty graph
    - parses text file into individual words and calls graph functions for each word to create a graph 
    - outputs final graph
'''
if __name__=="__main__":
    g_in = Graph()
    f_in = input("enter an input text file: ")
    out = populate(g_in, f_in)
    # fout = open(f_in, 'r')
    # lines = fout.readlines()
    # i = 1
    # for line in lines:
    #     #print("{}: {}".format(i, line))
    #     print("line: ", len(line))
    #     i += 1