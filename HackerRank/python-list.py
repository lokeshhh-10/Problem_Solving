if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        cmd = str(input()).split(" ")
        if cmd[0] == 'insert':
            list.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'append':
            list.append(int(cmd[1]))
        elif cmd[0] == 'remove':
            list.remove(int(cmd[1]))
        elif cmd[0] == 'sort':
            list = sorted(list)
        elif cmd[0] == 'pop':
            poped_element = list.pop()
        elif cmd[0] == 'reverse':
            list.reverse()
        elif cmd[0] == 'print':
            print(list)
