def solution(genres, plays):
    # 노래 목록 생성
    songs = []
    for i in range(len(genres)):
        songs.append({ 'id': i, 'genre': genres[i], 'play': plays[i] })

    # 재생 많이한 순서로 노래 목록 정렬
    songs.sort(key=lambda x: x['play'], reverse=True)

    # 장르별 재생 횟수 매핑
    total_plays = {}
    for i in range(len(plays)):
        genre = genres[i]
        if genre in total_plays:
            total_plays[genre] += plays[i]
        else:
            total_plays[genre] = plays[i]

    # 재생 횟수 순으로 장르 정렬
    sorted_genre_play_tuples = sorted([(g, total_plays[g]) for g in total_plays], key=lambda g: g[1], reverse=True)

    # 장르별로 노래 최대 2곡 수록
    answer = []
    for (genre, _) in sorted_genre_play_tuples:
        sorted_songs = [song['id'] for song in songs if song['genre'] == genre]
        answer += sorted_songs[:2]
    
    return answer
