import sys

print(sys.stdin.encoding)

# 파이썬은 들여쓰기가 생명
for i in range(1, 10):
    for j in range(1, 10):
        print("{} x {} = {}".format(i, j, i*j))


def greeting():
    print("Hello")


greeting()
