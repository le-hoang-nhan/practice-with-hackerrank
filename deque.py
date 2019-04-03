from collections import deque
if __name__ == "__main__":
    n = int(input())
    d = deque()
    for i in range(n):
        x = input().split()
        command = x[0]
        if command == "append":
            d.append(int(x[1]))
        if command == "appendleft":
            d.appendleft(int(x[1]))
        if command == "pop":
            d.pop()
        if command == "popleft":
            d.popleft() 
    print(*[item for item in d])
