def solution(name):
    answer = 0
    move = len(name) - 1
    next = 0

    for i, alpha in enumerate(name):
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        move = min(move, 2*i + len(name) - next)
    answer += move
    return answer
