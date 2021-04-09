class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Log:
    def __init__(self, cmd, user):
        self.cmd = cmd
        self.user = user

    def to_msg(self):
        msg_dict = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}
        return f"{self.user.name}님이 {msg_dict[self.cmd]}"


def solution(record):
    users = {}
    logs = []
    for x in record:
        split_x = x.split()
        cmd, id, name = split_x[0], split_x[1], split_x[2] if len(split_x) > 2 else None
        user = users.get(id)
        if cmd != 'Leave' and user:
            user.name = name
        elif cmd == 'Enter':
            user = User(id, name)
            users[id] = user
        if cmd != 'Change':
            logs.append(Log(cmd, user))

    return [x.to_msg() for x in logs]


if __name__ == '__main__':
    print(solution([
        "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"
    ]))
