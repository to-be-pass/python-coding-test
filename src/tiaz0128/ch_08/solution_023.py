from collections import Counter, defaultdict


def solution(genres, plays):
    answer = []
    gen_dict = defaultdict(list)
    play_count = Counter()

    # 각 장르별 노래의 재생 횟수를 누적합니다.
    for id, (gen, cnt) in enumerate(zip(genres, plays)):
        gen_dict[gen].append((id, cnt))
        play_count[gen] += cnt

    # 장르별 누적 재생 횟수를 기준으로 내림차순 정렬합니다.
    genres_rank = sorted(play_count.items(), key=lambda x: -x[1])

    # 각 장르별로 노래를 재생 횟수와 고유 번호에 따라 정렬하여 최대 2개씩 선택합니다.
    for gen, _ in genres_rank:
        gen_dict[gen] = sorted(gen_dict[gen], key=lambda x: (-x[1], x[0]))[:2]

    # 장르별로 선택된 노래를 answer 리스트에 추가합니다.
    for gen, _ in genres_rank:
        for id, _ in gen_dict[gen]:
            answer.append(id)

    return answer
