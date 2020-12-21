import pandas as pd
import networkx as nx


class Graph:
    def __init__(self, nodes=None, edges=None):
        # Initialises our nodes, edges and graphing info for Graph class
        # graphing info laid out such that : {node : {neighbour : cost}, node2 : {neighbour : cost2}...}
        self.nodes = []
        self.edges = []
        self.graphing = {}
        self.time = []
    
    def add_router(self, start_point, end_point, cost):
        #Inserts given router names and edges into respective lists
        if start_point not in self.nodes:
            self.nodes.append(start_point)
            self.graphing[start_point] = {}
        if end_point not in self.nodes:
            self.nodes.append(end_point)
            self.graphing[end_point] = {}
        self.graphing[start_point][end_point] = cost
        self.graphing[end_point][start_point] = cost
        self.edges.append((start_point, end_point))
        self.edges.append((end_point, start_point))
        self.time.append(cost)
        self.time.append(cost)

    def draw_graph(self):
        # Function utilizing NetorkX to display a graph of our router network
        G = nx.Graph()
        i = 0
        time = self.time
        while i < (len(self.edges)):
            G.add_edge(self.edges[i][0], self.edges[i][1], weight=time[i])
            i+= 1
        nx.draw(G, with_labels=True)


class Router:
    def __init__(self, router_name, graph):
        self.router_name = router_name
        self.graph = graph


    def get_path(self, destination):
        path, cost = self.dijkstra(self.router_name, destination)
        print("Start: {}\nEnd: {}\nPath: {}\nCost: {}\n".format(path[0], path[len(path) - 1], "->".join(path), cost))

    def insert(self, nodes, value):
        distances = {}
        for i in nodes:
            distances[i] = value
        return distances

    def dijkstra(self, start, goal):
        # Implementation of dijkstra algorithm. Set all nodes distance to infinity bar starting node. Set current
        # node to next nearest node and compare current distance of node to neighbors weight. Mark current node as visited, and repeat the process.
        distances = self.insert(graph.nodes, 9999999999)
        previous = self.insert(graph.nodes, None)
        unvisited = graph.nodes
        remaining = self.insert(graph.nodes, 9999999999)
        visited = []
        distances[start] = 0
        while len(visited) < len(unvisited):
            nearest = min(remaining, key = distances.get)
            visited.append(nearest)
            for node in graph.graphing[nearest]:
                if distances[node] > distances[nearest] + graph.graphing[nearest][node]:
                    distances[node] = distances[nearest] + graph.graphing[nearest][node]
                    previous[node] = nearest
            remaining.pop(nearest)
        
        # If distance still infinite, goal is unreachable. Else, use previous list to backtrack to start to find path taken
        if distances[goal] != 9999999999:
            path = [goal]
            if path != None:
                while start not in path:
                    path.append(previous[path[-1]])
                path.reverse()
        else:
            path = None
            distances[goal] = 0
        return path, distances[goal]
    
    
    def remove_router(self, router_name):
        graph.nodes.remove(router_name)
        del graph.graphing[router_name]
        for key in graph.graphing:
            if router_name in graph.graphing[key]:
                del graph.graphing[key][router_name]
        
        return router.print_routing_table()

    def print_routing_table(self):
        fromlist = []
        to = []
        costs = []
        route = []
        for i in graph.nodes:
            path, cost = self.dijkstra(self.router_name, i)
            costs.append(cost)
            if path != None:
                string = "->".join(path)
            else:
                string = "Unreachable"
            route.append(string)
            fromlist.append(self.router_name)
            to.append(i)
            
        data = {'from': fromlist, 'to': to, 'cost': costs, 'path': route}
        print(pd.DataFrame.from_dict(data))
        

    


if __name__ == '__main__':
    graph = Graph()
    graph.add_router("a", "b", 7)
    graph.add_router("a", "c", 9)
    graph.add_router("a", "f", 14)
    graph.add_router("b", "c", 10)
    graph.add_router("b", "d", 15)
    graph.add_router("c", "d", 11)
    graph.add_router("c", "f", 2)
    graph.add_router("d", "e", 6)
    graph.add_router("e", "f", 9)
    router = Router("a", graph)
    router = Router("a", graph)
    router_two = Router("b", graph)
    router.print_routing_table()
    router_two.print_routing_table()
    router.remove_router("c")
    router_two.print_routing_table()
    graph.draw_graph()
    

    
    

