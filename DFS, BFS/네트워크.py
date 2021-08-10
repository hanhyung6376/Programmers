def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            answer += dfs(n ,i, visited, computers)
    return answer


def dfs(n, now, visited, computers):
    visited[now] = True

    for i in range(n):
        if visited[i] == False and computers[now][i] == 1:
            dfs(n, i, visited, computers)
    return 1