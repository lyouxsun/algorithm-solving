# convention
- 배열 : arr
- 집합 : s
- 좌표 변수 : x, y

- 2차원 배열 : `arr[row 인덱스][column 인덱스]`
- 3차원 배열 : `arr[depth 인덱스][row 인덱스][column 인덱스]`


- 파이썬 빠른 입출력!
  ```python
  import sys
  input = sys.stdin.readline
  
  n = int(input())
  a, b = map(int, input().split())
  ```

- 재귀함수 사용 시 넣어줘야 할 코드
```python
    sys.setrecursionlimit(10 ** 6)
```

- 입력개수가 주어지지 않은 경우 무한루프 끝내는 방법
```python
    while True:
        try:
            n, m = map(int, input().split())        # 입력받는 부분
        except (ValueError, EOFError):
            exit()
```