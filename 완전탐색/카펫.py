def solution(brown, yellow):
    answer = []
    arr = [[yellow // i, i] for i in range(1, int(yellow ** 0.5) + 1) if yellow % i == 0]

    for r, c in arr:
        if (r + 2) * (c + 2) == brown + yellow:
            return [r + 2, c + 2]

    return answer