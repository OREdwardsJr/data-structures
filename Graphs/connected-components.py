def build_graph(edges) -> dict[list]:
    graph = {}
    for start, end in edges:
        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []
        graph[start].append(end)
        if start != end:
            graph[end].append(start)

    return graph


# graph = build_graph(edges)
graph = {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}


def components(graph) -> int:
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, current, visited):
    if str(current) in visited:
        return False

    visited.add(str(current))

    for node in graph[current]:
        explore(graph, node, visited)

    return True


print(components(graph))
