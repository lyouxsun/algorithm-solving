a = int(input())
for i in range(a):
    for j in range(a):
        if i != 0 and j % 2 == 0:
            print(end = '  ')
            continue
        if j >= i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()