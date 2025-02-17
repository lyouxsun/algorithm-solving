def solution(citations):
    answer = 0
    citations.sort(reverse = True) 
    for num, citation in enumerate(citations):
        if citation >= num+1: 
            h_index = num+1
            answer = h_index

    return answer