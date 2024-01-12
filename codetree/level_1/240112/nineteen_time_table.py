for i in range(1, 20):
    for j in range(1, 20):
        print(f'{i} * {j} = {i*j}', end = '')
        if j==19 or (j % 2 == 0):
            print()
            continue
        print(' / ', end='')