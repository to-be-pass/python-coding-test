def solution(phone_book):
    phone_book.sort()

    for idx, phone in enumerate(phone_book):
        if idx != 0 and phone.startswith(phone_book[idx - 1]):
            return False

    return True
