edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]


# Build adjacency list - my way O(n) time-complexity.. decent?
graph = {}
for start, end in edges:
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    graph[start].append(end)
    graph[end].append(start)

# Iterative
def has_path(start, end, graph):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            for elem in graph[node]:
                stack.append(elem)

    return False


# Recursive
def has_path(start, end, graph, visited=set()):
    visited = visited

    if start == end:
        return True

    if start in visited:
        return False

    visited.add(start)
    for node in graph[start]:
        if has_path(node, end, graph, visited) == True:
            return True


print(has_path("j", "m", graph) == True)
print(has_path("i", "n", graph) == False)
print(has_path("i", "o", graph) == False)
print(has_path("o", "n", graph) == True)
print(has_path("n", "o", graph) == True)
