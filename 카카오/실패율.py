import heapq

def solution(N, stages):
    answer = []
    heap, arr = [], [0] * (N + 2)
    total = len(stages)
    for i in stages:
        arr[i] += 1
    for i in range(1, N + 1):
        if arr[i] == 0:
            heapq.heappush(heap, [0, 0, i])
        else:
            heapq.heappush(heap, [- arr[i] / total, arr[i] / total, i])
        total -= arr[i]

    while heap:
        score1, score2, num = heapq.heappop(heap)
        answer.append(num)
    return answer