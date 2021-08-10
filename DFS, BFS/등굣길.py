from collections import deque


def solution(m, n, puddles):
    answer = 0
    matrix = [[0 for i in range(m)] for j in range(n)]

    for c, r in puddles:
        matrix[r - 1][c - 1] = -1
    bfs(matrix, m, n)
    answer = matrix[n - 1][m - 1]
    return answer % 1000000007


def bfs(matrix, m, n):
    queue = deque()
    queue.append([0, 0])
    matrix[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] != -1:
                    matrix[nx][ny] += matrix[x][y]
                    if [nx, ny] not in queue:
                        queue.append([nx, ny])


dx = [1, 0]
dy = [0, 1]