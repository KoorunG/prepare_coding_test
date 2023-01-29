# DFS 구현

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

# 1. 재귀로 구현
def dfs_with_recursive(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = dfs_with_recursive(w, discovered)
    return discovered

print(dfs_with_recursive(1)) # [1, 2, 5, 6, 7, 3, 4]


# 2. 스택으로 구현
def dfs_with_iterate(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(dfs_with_iterate(1)) # [1, 4, 3, 5, 7, 6, 2]