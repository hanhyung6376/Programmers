from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    user_id.sort
    banned_id.sort
    arr = list(permutations(user_id, len(banned_id)))
    result = []

    for user_list in arr:
        isTrue = True
        for user, ban in zip(user_list, banned_id):
            if len(user) != len(ban):
                isTrue = False
                break
            for u, b in zip(user, ban):
                if len(u) != len(b):
                    isTrue = False
                    break
                elif b != '*' and u != b:
                    isTrue = False
                    break
        # 중복 제거
        if isTrue and sorted(user_list) not in result:
            result.append(sorted(user_list))

    answer = len(result)

    return answer
