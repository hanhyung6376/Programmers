def solution(table, languages, preference):
    answer = ''
    lang_score = {}
    max_score = 0
    for lang, pref in zip(languages, preference):
        lang_score[lang] = pref
    score = [5, 4, 3, 2, 1]
    for i in table:
        job = i.split()
        job_score = 0
        for j in job[1:]:
            if j in lang_score:
                job_score += lang_score[j] * score[job.index(j) - 1]
        if job_score > max_score:
            max_score = job_score
            answer = job[0]
        elif job_score == max_score:
            word = [job[0], answer]
            word.sort()
            answer = word[0]

    return answer

