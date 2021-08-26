def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])

    def find(target):
        if target == parent[target]:
            return parent[target]

        parent[target] = find(parent[target])
        return parent[target]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def kruskal():
        tree_edges = 0
        cost = 0
        for u, v, w in costs:
            if find(u) != find(v):
                union(u, v)
                cost += w
        return cost

    answer = kruskal();

    return answer

