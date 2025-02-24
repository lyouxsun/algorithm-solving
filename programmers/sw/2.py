# 1 ~ n 에서 k개의 수를 고름
# questions : q/a = q 이상인 수는 a개이다.

def solution(n, k, questions):
      cand = [[i for i in range(1, n+1)] for i in range(k)]
      
      for (q, a) in questions:
      # 뒤에 a개 후보 자르기 (~~ 이상이어야함)
            for idx in range(a):
                  cand[k-idx-1] = [i for i in range(max(q, cand[k-idx-1][0]),cand[k-idx-1][-1]+1)]
      
      
      # 앞에 k-a개 후보 자르기 (~~ 이하여야함)
      for idx in range(k-a):
            cand[idx] = [i for i in range(cand[idx][0], min(q-1, cand[idx][-1])+1)]
      
      for c in cand:
            print(c)
      print()
      
      
      answer = []
      i = 0
      while i < k:
            if len(answer) >= i+1:
                  i += 1
                  continue
            flag = True
            cnt = 0
            while i+1 < k and cand[i] == cand[i+1]:
                  cnt += 1
                  i += 1
                  flag = False
                  for j in range(cnt+1):
                        answer.append(len(cand[i-j])-cnt)
      
         # print('i=', i, ', answer=', answer)
         
            if flag:
                  i += 1
      return answer