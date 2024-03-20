
def solution(N, stages):
    mole, denom = [0] * N, [0] * N 
    for s in stages:
        # 스테이지에 도달한 플레이어 수
        for i in range(s):
            try:
                denom[i] += 1
            except:
                denom[-1] += 1
        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        try:
            mole[s - 1] += 1
        except:
            mole[-1] + 1

    zipped = [m / d if d != 0 else 0 for m, d in zip(mole, denom)]
    return [x[0] for x in sorted([(i + 1 , r) for i, r in enumerate(zipped)], key=lambda x: x[1], reverse = True)]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))