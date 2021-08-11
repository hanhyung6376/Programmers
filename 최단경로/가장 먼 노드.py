import heapq

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n + 1)]

    for i, j in edge:
        graph[i].append([j, 1])
        graph[j].append([i, 1])
    dp = dijkstra(graph, n)
    max_value = max(dp)
    answer = dp.count(max_value)
    return answer


def dijkstra(graph, n):
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[1] = 0
    heap = []
    heapq.heappush(heap, [1, 0])
    while heap:
        now, now_weight = heapq.heappop(heap)

        for next, weight in graph[now]:
            next_weight = now_weight + weight

            if dp[next] > next_weight:
                dp[next] = next_weight
                heapq.heappush(heap, [next, next_weight])
    dp = [i if i != inf else 0 for i in dp]
    return dp
