def solution(n, s, a, b, fares):
    inf = float('inf')
    answer = inf
    graph = [[inf if i !=j else 0 for i in range(n+1)] for j in range(n+1)]
    for u, v, w in fares:
        graph[u][v] = w
        graph[v][u] = w
    floyd_warshall(graph)

    for i in range(1, n+1):
        if answer > graph[s][i] + graph[i][a] + graph[i][b]:
            answer = graph[s][i] + graph[i][a] + graph[i][b]

    answer = min(answer, graph[s][a] + graph[a][b], graph[s][b] + graph[b][a])
    return answer


def floyd_warshall(graph):
    for k in range(1, len(graph)):
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j]  = graph[i][k] + graph[k][j]