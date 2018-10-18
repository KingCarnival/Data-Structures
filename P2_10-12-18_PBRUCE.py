# This code is modified from code posted on https://www.geeksforgeeks.org/graph-and-its-representations/

class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
  
# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 
  
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    V = 10
    graph = Graph(V) 
    # A row connections
    graph.add_edge(0, 0) 
    graph.add_edge(0, 2) 
    graph.add_edge(0, 3)
    graph.add_edge(0, 4)

    # B row Connections
    graph.add_edge(1, 5)
    graph.add_edge(1, 6)

    # C row Connections  
    graph.add_edge(2, 3) 
    graph.add_edge(2, 5)

    # D Row
    graph.add_edge(3, 2)
    
    # E Row
    graph.add_edge(4, 1)
    graph.add_edge(4, 5)

    # F Row
    graph.add_edge(5, 1)
    graph.add_edge(5, 2)
    graph.add_edge(5, 4)

    # G Row
    graph.add_edge(6, 7)
    graph.add_edge(6, 9)

    # H Row
    graph.add_edge(7, 8)

    # I Row
    graph.add_edge(8, 9)
  
    graph.print_graph() 
  
# This code is contributed by Kanav Malhotra 