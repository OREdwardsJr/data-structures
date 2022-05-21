'''
An adjacency list is a data structure that maps edges to nodes.

Example of an adjacency list
    {
        "a": ["b", "c", "d"],
        "b": ["a"]
        "c": ["a", "d"]
        "d": ["a", "c"]
    }

The data structure is composed of a dictionary where the node is stored as the key and the edges
are stored in an array.

It is often the format utilized before traversing a graph
'''

# Example of a function building an adjacency list
edges = [
    ("a", "b"),
    ("b", "a"),
    ("a", "c"),
    ("c", "a"),
    ("a", "d"),
    ("d", "a"),
    ("c", "d"),
    ("d", "c")
]

graph_data = {}

for start, end in edges:
    if start not in graph_data:
        graph_data[start] = [end]
    else:
        graph_data[start].append(end)

print(graph_data)