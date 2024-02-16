def solution(n, words):
    word_set = set()
    for i in range(len(words)):
        word = words[i]
        prev = words[i - 1] if i > 0 else None
        if word in word_set or (prev and prev[-1] != word[0]):
            man = (i % n) + 1
            turn = (i // n) + 1
            return [man, turn]
        else:
            word_set.add(word)
    return [0, 0]
