from itertools import permutations

n = int(input())  
arr = [i for i in range(1, n+1)]  
combs = permutations(arr) 
answer = []

def is_valid_stack_sequence(sequence):
    stack = []
    index = 0  
    for num in sequence:
        while index < num:  
            index += 1
            stack.append(index)
        if stack[-1] == num:  
            stack.pop()
        else:
            return False  
    return True

for comb in combs:
    if is_valid_stack_sequence(comb):
        answer.append(comb)

answer.sort()

for ans in answer:
    print(' '.join(map(str, ans)))
