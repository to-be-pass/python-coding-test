# O(N) : 정답과 비교하기
def solution(answers):
    one_raw=[1,2,3,4,5]
    one=[one_raw[i%5] for i in range(0,len(answers))]
    two_raw=[2,1,2,3,2,4,2,5]
    two=[two_raw[i%8] for i in range(0,len(answers)) ]
    three_raw=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    three=[three_raw[i%10] for i in range(0,len(answers))]
    counts=[0,0,0]
    for a,b,c,d in zip(one,two,three,answers):
        if a==d : counts[0]+=1
        if b==d : counts[1]+=1
        if c==d : counts[2]+=1
    answer=[]
    for index,i in enumerate(counts):
        if i==max(counts):answer.append(index+1)
    return answer