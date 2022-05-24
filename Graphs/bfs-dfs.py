from collections import deque

graph = {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def bfs(graph: dict, source) -> list:
    q = deque([source])
    output = []

    while q:
        node = q.popleft()
        output.append(node)
        q.extend([*graph[node]]) # A for loop would work here too

    return output


def dfs(graph: dict, source) -> list:
    output = [source]
    stack = [*graph[source]]

    while stack:
        node = stack.pop()
        output.append(node)
        if graph[node]:
            stack.append(*graph[node])

    return output


print(dfs(graph, "a"))
print(bfs(graph, "a"))
