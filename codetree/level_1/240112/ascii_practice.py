num = int(input())
alphabet = ord('A')

for i in range(num):
    for j in range(i):
        print(chr(alphabet), end='')
        alphabet += 1
        if alphabet > ord('Z'):
            alphabet = ord('A')
    print()