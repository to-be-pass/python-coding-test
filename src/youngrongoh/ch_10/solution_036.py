def solution(phone_book):
    sorted_book = sorted(phone_book)
    for i in range(len(sorted_book) - 1):
        if sorted_book[i] == sorted_book[i+1][:len(sorted_book[i])]:
                return False
    return True
