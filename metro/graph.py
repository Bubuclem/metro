from collections import defaultdict, deque
import math
from .models import Station, Trajet
from .commun import TimeEntry, Print_value, start_timer, stop_timer

#Globales
Values_print = Print_value()

# Solution n°1
class Graph_1(object):
    def __init__(self):
        self.stations = set()
        self.trajets = defaultdict(list)
        self.distances = {}
        self.time = 0

    def add_station(self, value):
        self.stations.add(value)

    def add_trajet(self, from_station, to_station):
        self.trajets[from_station].append(to_station)
        self.trajets[to_station].append(from_station)
        x = from_station.x_coord - to_station.x_coord
        y = from_station.y_coord - to_station.y_coord
        distance = math.pow(x, 2) + math.pow(y, 2)
        self.distances[(from_station, to_station)] = math.sqrt(distance)

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    stations = set(graph.stations)

    while stations:
        min_station = None
        for station in stations:
            if station in visited:
                if min_station is None: 
                    min_station = station 
                elif visited[station] < visited[min_station]:
                    min_station = station
        if min_station is None: 
            break

        stations.remove(min_station)
        current_weight = visited[min_station]

        for trajet in graph.trajets[min_station]:
            try:
                weight = current_weight + graph.distances[(min_station, trajet)]
            except:
                continue
            if trajet not in visited or weight < visited[trajet]:
                visited[trajet] = weight
                path[trajet]    = min_station

    return visited, path

def shortest_path(graph, origin, destination):
    visited, paths  = dijkstra(graph, origin)
    full_path       = deque()
    _destination    = paths[destination]
    
    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

def graph_test():
    graph = Graph_1()

    all_stations = Station.objects.all()

    for station in all_stations:
        graph.add_station(station)

    for station in all_stations:
        trajets = Trajet.objects.filter(FromStation=station)
        for trajet in trajets:
            graph.add_trajet(trajet.FromStation, trajet.ToStation)

    orgin                       = Station.objects.get(nom="Cuire")
    destination                 = Station.objects.get(nom="Cusset")
    path_distance, path_list    = shortest_path(graph,orgin, destination)

    return path_distance, path_list

def get_path(start, end):
    graph = Graph_1()

    all_stations = Station.objects.all()

    for station in all_stations:
        graph.add_station(station)

        trajets = Trajet.objects.filter(FromStation=station)
        for trajet in trajets:
            graph.add_trajet(trajet.FromStation, trajet.ToStation)

    orgin                     = Station.objects.get(pk=start.id)
    destination               = Station.objects.get(pk=end.id)
    path_distance, path_list  = shortest_path(graph, orgin, destination)

    return path_distance, path_list

# Solution n°2
def bellman_ford(graph, source):
    distance, predecesseur = dict(), dict()
    for u in graph:
        distance[u], predecesseur[u] = float('inf'), None
    distance[source] = 0

    #for _ in range(len(graph) - 1):
    #    for u in graph:
    #        for neighbour in graph[u]:
    #            Values_print.add_message(neighbour)
    #            #Values_print.add_message(graph[u][neighbour])
    #            if distance[neighbour] > distance[u] + graph[u][neighbour]:
    #                distance[neighbour], predecesseur[neighbour] = distance[u] + graph[u][neighbour], u

    #for u in graph:
    #    for v in graph[u]:
    #        assert distance[v] <= distance[u] + graph[u][v], "Negative weight cycle."
 
    return distance, predecesseur

def graph_test_2():
    graph = {
        'a': {'b': 1, 'c':  4},
        'b': {'c': 3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b': 1, 'c':  5},
        'e': {'d': 3},
        'f': {'d': 5}
        }

    destination, predecesseur = bellman_ford(graph, 'a')

    return destination, predecesseur

def get_path_2(depart,arrive):
    
    graph = {}
    
    all_stations = Station.objects.all()

    for station in all_stations:
        trajets = Trajet.objects.filter(FromStation=station)
        for trajet in trajets:
            graphstation = {
                station.nom : { trajet : trajet.distance }
            }
        graph[station] = graphstation

    destination, predecesseur = bellman_ford(graph, depart.nom)

    return destination, predecesseur

# Autre
def print_values():
    return ", ".join([str(m) for m in Values_print.messages])