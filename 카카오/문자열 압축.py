def solution(s):
    answer = 1001
    cnt = 1
    # 길이가 1일 경우에는 압축 불가능
    if len(s) == 1:
        return 1
    while cnt <= len(s) // 2:
        result = ''
        length = 1
        change = s[:cnt]

        for i in range(cnt, len(s) + cnt, cnt):
            if change == s[i: i + cnt]:
                length += 1
            else:
                if length == 1:
                    result += change
                else:
                    result += str(length) + change
                change = s[i: i + cnt]
                length = 1
        answer = min(answer, len(result))
        cnt += 1
    return answer