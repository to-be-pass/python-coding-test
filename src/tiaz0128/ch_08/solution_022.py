def solution(record):
    answer = []
    users = {}

    command_string = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for row in record:
        command, user_id, *alias = row.split(" ")

        if command in ["Enter", "Change"]:
            users[user_id] = alias[0]

        if command in ["Enter", "Leave"]:
            answer.append("{" + user_id + "}" + command_string[command])

    return [row.format(**users) for row in answer]
