# BFS 구현

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

# 1. 큐로 구현 (재귀로 구현하는 방법은 없다)
def bfs_whth_iterate(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

print(bfs_whth_iterate(1)) # [1, 2, 3, 4, 5, 6, 7]