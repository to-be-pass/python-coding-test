def solution(answers):
    ptns = ['12345', '21232425', '3311224455']
    scores = [0, 0, 0]
    for i, answer in enumerate(answers):
        for j, ptn in enumerate(ptns):
            ptnIdx = i % len(ptn)
            if answer == int(ptn[ptnIdx]):
                scores[j] += 1
    max_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if max_score == score]
