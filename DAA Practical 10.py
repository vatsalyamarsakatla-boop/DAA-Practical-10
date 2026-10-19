
V = 5

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

edges.sort(key=lambda x: x[2])

parent = list(range(V))
rank = [0] * V

def find_parent(i):
    if parent[i] != i:
        parent[i] = find_parent(parent[i])
    return parent[i]

def union_set(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

total = 0
count = 0

print("Edges in MST:")

for u, v, weight in edges:
    root_u = find_parent(u)
    root_v = find_parent(v)

    if root_u != root_v:
        print(u, "-", v, ":", weight)
        total += weight
        union_set(root_u, root_v)
        count += 1

    if count == V - 1:
        break

print("Total weight of MST =", total)
print("EN.No: 92460118673")