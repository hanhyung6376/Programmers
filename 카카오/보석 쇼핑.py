from collections import defaultdict


def solution(gems):
    answer = [0, len(gems)]
    start, end = 0, 0
    set_gems = len(set(gems))
    gems_dict = defaultdict(int)
    gems_dict[gems[0]] = 1

    while start < len(gems) and end <= len(gems):
        if len(gems_dict) == set_gems:
            if answer[1] - answer[0] > end - start:
                answer = [start + 1, end + 1]

            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            gems_dict[gems[end]] += 1

    return answer