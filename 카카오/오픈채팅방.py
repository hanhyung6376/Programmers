def solution(record):
    answer = []
    user_dict = {}
    # 유저 닉네임 매칭
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            user_dict[r[1]] = r[2]
        elif r[0] == 'Change':
            user_dict[r[1]] = r[2]
    # 로그 생성
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer.append(f'{user_dict[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(f'{user_dict[r[1]]}님이 나갔습니다.')

    return answer