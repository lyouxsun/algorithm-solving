# 파이썬 컬렉션/모듈 정리

## 목차

# 1. Priority Queue (우선순위 큐)

- `import heapq`

  heapq 모듈을 사용하여 우선순위 큐를 구현할 수 있다.
- heapq 모듈은 최소 힙(min heap)이다. 부모 노드가 자식 노드의 값보다 작거나 같다.
- 힙의 리프노드는 왼쪽부터 빠짐없이 채워나간다. (레벨 순서로 노드를 삽입한다.)
- heapq 모듈 사용법
    - q 리스트를 미리 선언 및 초기화
    - `heapqpush(q, data)` 메서드를 통해 데이터를 삽입
    - `heappoop(q)` 메서드를 통해 데이터 삭제
    - `heapify(arr)` : 주어진 리스트를 힙 구조로 변환한다. (반환값 없이 arr를 변환한다.)

# 2. Deque

'ChainMap',
'Counter',
'OrderedDict',
'UserDict',
'UserList',
'UserString',
'defaultdict',
'deque',
'namedtuple',
