def solution(n, words):
    word_set = set()

    for idx, word in enumerate(words):
        if word in word_set:
            return [idx % n + 1, idx // n + 1]

        if idx != 0 and words[idx - 1][-1] != word[0]:
            return [idx % n + 1, idx // n + 1]

        word_set.add(word)

    return [0, 0]
