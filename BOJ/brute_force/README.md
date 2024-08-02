# Brute Force

## 문제 풀이

| 번호 |    날짜    | 문제 번호                                              | 풀이법                                                         | 주의사항                                                            | 새롭게 배운 내용                                                                                          | 다시 풀어보기 |
|:--:|:--------:|:---------------------------------------------------|:------------------------------------------------------------|:----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|:-------:|
| 1  | 24.07.29 | [BOJ 16917](https://www.acmicpc.net/problem/16917) | 반반치킨이 0마리 ~ 최대마리수 인 모든 경우를 고려하여 최소 가격 구하기                   | 반반치킨이 비싼 경우는 가지치기 (반반치킨 무시한 결과 출력 후 바로 종료)                      | - `max(0, 어떤값)` : 음수 방지  <br> - 내가 구해야 하는 값, 답을 구하는 데 계속 변화하는 값에 집중하자!                             |         |
| 2  | 24.07.29 | [BOJ 16968](https://www.acmicpc.net/problem/16968) | 쉽고 간단한 브루트 포스 문제                                            |                                                                 |                                                                                                    |         |
| 3  | 24.07.29 | [BOJ 16922](https://www.acmicpc.net/problem/16922) | 식1) a+b+c+d = 인풋!  식2) a+5b+10c+50d = (만들 수 있는 숫자) 식 세워서 구함 | 4중 for문 사용,, 더 나은 풀이법 찾기!                                       |                                                                                                    |         |
| 4  | 24.07.30 | [BOJ 16936](https://www.acmicpc.net/problem/16936) | 입력받은 리스트에서 숫자 하나씩 가져와서 정답 리스트 맨앞 or 맨뒤에 하나씩 붙이기             | 나눗셈으로 조건 따지면 (1. 나눠 떨어지는가 -> 2. 그 때의 몫) 계산이 길어져서, 그냥 모두 곱셈으로 구현 | `list.pop()` 의 파라미터에는 값(x) 인덱스(o) 가 들어가야한다.                                                        |         |
| 5  | 24.07.31 | [BOJ 16943](https://www.acmicpc.net/problem/16943) | A 배열로 만들 수 있는 모든 숫자열 만들기 -> 모두 B랑 비교해서 그 중 가장 큰 수 출력        | 파이썬의 메서드 잘 활용하자!                                                | `from itertools import permutations` -> `permutations(arr)` : 입력된 iterable의 요소들로 만들 수 있는 모든 순열을 생성 |         |
| 6  | 24.08.01 | [BOJ 16924](https://www.acmicpc.net/problem/16924) | '*' 인 모든 부분을 십자가의 중심이라 생각하며 반복하기                            | 브루트 포스를 풀 때에는 모든 요소에 일관되게 적용할 수 있는 조건이 무엇인지 고민해보기!              | `list(input())` 이렇게 입력 받으면 이어진 문자열을 리스트에 한 글자씩 저장할 수 있다.                                           |    ✅    |
| 7  | 24.08.02 | [BOJ 1476](https://www.acmicpc.net/problem/1476)   | 구해야 하는게 뭔지!! 항상 생각해                                         |                                                                 |                                                                                                    |         |