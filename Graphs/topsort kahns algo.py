from collections import defaultdict, deque


edges = [
    (13, 13),
    (9, 2),
    (9, 10),
    (2, 6),
    (0, 2),
    (0, 6),
    (0, 3),
    (3, 1),
    (3, 4),
    (1, 4),
    (4, 5),
    (4, 8),
    (5, 5),
    (6, 7),
    (6, 11),
    (10, 6),
    (7, 4),
    (7, 12),
    (11, 12),
    (12, 8),
    (8, 8),
]

adj_list = defaultdict(list)

for s, e in edges:
    if s == e:
        adj_list[s] == []
    else:
        adj_list[s] += [e]

order = [0] * len(adj_list)

for value in adj_list.values():
    for i in value:
        order[i] += 1

q = deque([])

for i in range(len(order)):
    if not order[i]:
        q += [i]
        order[i] = -1

topological_order = []

while q:
    node = q.popleft()
    topological_order.append(node)
    #Decrease nodes that were dependent on node
    for i in adj_list[node]:
        order[i] -= 1
    #Add any nodes with 0 dependencies to q
    for i in range(len(order)):
        if not order[i]:
            q += [i]
            order[i] = -1


print(topological_order)