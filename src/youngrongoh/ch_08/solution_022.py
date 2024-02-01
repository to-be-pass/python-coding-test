cmd_message = {
    'Enter': '{name}님이 들어왔습니다.',
    'Leave': '{name}님이 나갔습니다.',
}

def solution(record):
    users = {}
    for log in record:
        params = log.split()
        if len(params) > 2:
            users[params[1]] = params[2]

    messages = []
    for log in record:
        params = log.split()
        if params[0] in cmd_message:
            messages.append(cmd_message[params[0]].format(name=users[params[1]]))
    return messages

