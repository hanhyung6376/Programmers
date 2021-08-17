def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    B_idx, A_idx = 0, 0
    if B[0] < A[-1]:
        return 0

    while True:
        if B[B_idx] > A[A_idx]:
            answer += 1
            B_idx += 1
            A_idx += 1
        elif B[B_idx] <= A[A_idx]:
            A_idx += 1

        if B_idx == len(B) or A_idx == len(A):
            break

    return answer