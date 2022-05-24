from collections import deque

graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}

"""
We want to build an algorithm that determines whether a path is present between two nodes.
Return True if path exists and False if path doesn't exist.

Either BFS or DFS works


- Check whether our root is the value we're searching for
    - Return True if so
- Add root to q
- Pop item from q
- Add children
- Continue until we have found our key or ran out of nodes.
"""

""" BREADTH FIRST SEARCH """
# Iterative Approach
def has_path_bfs(start, end, graph, q=deque([])) -> bool:
    q = deque([start])

    while q:
        node = q.popleft()
        if node == end:
            return True
        q.extend([*graph[node]])

    return False


print(has_path_bfs("f", "g", graph) == True)
print(has_path_bfs("f", "h", graph) == True)
print(has_path_bfs("f", "i", graph) == True)
print(has_path_bfs("f", "j", graph) == False)
print(has_path_bfs("f", "k", graph) == True)


""" DEPTH FIRST SEARCH """
"""
#Iterative approach
def has_path_dfs(start, end, graph) -> bool:
    stack = [start]

    while stack:
        node = stack.pop()
        if node == end:
            return True
        for elem in graph[node]:
            stack.append(elem)

    return False


#Recursive Approach
def has_path_dfs(start, end, graph) -> bool:
    if start == end:
        return True

    for node in graph[start]:
        if has_path_dfs(node, end, graph) == True:
            return True

    return False

print(has_path_dfs("f", "g", graph) == True)
print(has_path_dfs("f", "h", graph) == True)
print(has_path_dfs("f", "i", graph) == True)
print(has_path_dfs("f", "j", graph) == False)
print(has_path_dfs("f", "k", graph) == True)
"""