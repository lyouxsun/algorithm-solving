# 자주 사용하는 라이브러리 & 함수 정리

## 1. math
- `math.gcd(a, b)`: 최대공약수
- `math.lcm(a, b)`: 최소공배수 (Python 3.9+)
- `math.factorial(n)`: n!
- `math.sqrt(x)`: 제곱근
- `math.ceil(x)`: 올림
- `math.floor(x)`: 버림
- `round(x)`: 반올림
- `abs(x)`: 절댓값
- `math.log(x, base)`: 로그 (기본은 자연로그)
- `round(x, n)`: 소수 n째 자리까지 반올림


## 2. sys
- 빠른 입력 (input()보다 훨씬 빠름)
  ```python
  import sys
  input = sys.stdin.readline
  ```
- 재귀 깊이 제한 설정 (DFS 등에서 RecursionError 방지)
  ```python
  import sys
  sys.setrecursionlimit(10**6)  # 기본 제한은 약 1000
  ```



## 3. 기본 내장 함수들
- `sorted(iterable, key=None, reverse=False)`: 정렬된 리스트를 반환 (원본은 그대로 유지)
- `sum(iterable)`: 모든 요소의 합
- `max(iterable)`: 가장 큰 값
- `min(iterable)`: 가장 작은 값
- `enumerate(iterable)`: 인덱스와 값을 함께 튜플로 반환
  ```python
  for i, value in enumerate(['a', 'b']):  # (0, 'a'), (1, 'b')
      ...
  ```
- `zip(a, b, ...)`: 여러 시퀀스를 병렬로 묶어줌
  ```python
  for a, b in zip([1, 2], ['a', 'b']):  # (1, 'a'), (2, 'b')
      ...
  ```
- `map(func, iterable)`: 각 요소에 함수를 적용
  ```python
  list(map(str, [1, 2, 3]))  # ['1', '2', '3']
  ```
- `filter(func, iterable)`: 조건을 만족하는 요소만 걸러냄
  ```python
  list(filter(lambda x: x % 2 == 0, [1, 2, 3]))  # [2]
  ```
- `any(iterable)`: 하나라도 True면 True
- `all(iterable)`: 모두 True면 True

## 4. bisect (이진 탐색 라이브러리)
- `bisect.bisect_left(a, x)`: x를 삽입할 수 있는 가장 왼쪽 인덱스
- `bisect.bisect_right(a, x)`: x를 삽입할 수 있는 가장 오른쪽 인덱스
- `bisect.insort_left(a, x)`: 정렬된 리스트 a에 x를 왼쪽 기준으로 삽입
- `bisect.insort_right(a, x)`: 정렬된 리스트 a에 x를 오른쪽 기준으로 삽입
  