"""
CREATE A CYCLIC, DIRECTED GRAPH REPRESENTING VARIOUS FLIGHT PATHS. 
"""

from turtle import st


routes = [
    ("Seattle", "Los Angeles"),
    ("Seattle", "New York"),
    ("Los Angeles", "Dallas"),
    ("Dallas", "Atlanta"),
    ("Atlanta", "Los Angeles"),
    ("Atlanta", "New York"),
    ("New York", "Seattle"),
    ("Orlando", "Bahamas"),
    ("Bahamas", "Orlando"),
]


class Graph:
    def __init__(self, edges: list[tuple]) -> None:
        self.graph = {}

        for start, end in edges:
            if start not in self.graph:
                self.graph[start] = [end]
            else:
                self.graph[start].append(end)

    def get_paths(self, start, end, path=[]) -> list:
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph:
            return None

        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]) -> list:
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph:
            return None

        shortest_path = None
        for node in self.graph[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if not shortest_path or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

flights = Graph(routes)

start = "Los Angeles"
end = "New York"
print(f"Paths from Los Angeles to New York: {flights.get_paths(start, end)}")


start = "Seattle"
end = "New York"
print(f"Paths from Seattle to New York: {flights.get_paths(start, end)}")
print()
print(
    f"The shortest path from Seattle to New York is : {flights.get_shortest_path(start, end)}"
)
print()

start = "Atlanta"
end = "Los Angeles"
print(f"Paths from {start} to {end}: {flights.get_paths(start, end)}")
print()
print(
    f"The shortest path from {start} to {end} is : {flights.get_shortest_path(start, end)}"
)
print()
