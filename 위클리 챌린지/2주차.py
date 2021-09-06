def solution(scores):
    answer = ''

    for i in range(len(scores)):
        score = [j[i] for j in scores]
        my_score = score[i]
        if score.count(my_score) >= 2:
            answer += return_score(sum(score) // len(score))
        else:
            if my_score == max(score) or my_score == min(score):
                answer += return_score((sum(score) - my_score) // (len(score)-1))
            else:
                answer += return_score(sum(score) // len(score))

    return answer

def return_score(score):
    print(score)
    if score >= 90:
        return 'A'
    elif score < 90 and score >= 80:
        return 'B'
    elif score < 80 and score >= 70:
        return 'C'
    elif score < 70 and score >= 50:
        return 'D'
    else:
        return 'F'
