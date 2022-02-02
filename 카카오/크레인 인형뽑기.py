def solution(board, moves):
    answer = 0
    stack = []
    check_board = [[] for i in range(len(board[0]))]

    for i in board:
        col = []
        for j in range(0, len(i)):
            if i[j] != 0:
                check_board[j].append(i[j])

    for i in moves:
        if check_board[i-1]:
            stack.append(check_board[i - 1][0])
            del check_board[i - 1][0]

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            answer += 2
            del stack[-1]
            del stack[-1]


    return answer
