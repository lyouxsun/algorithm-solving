# 정렬

## 목차
- [sort() 🆚 sorted()](#sort--sorted)
- [명시적으로 key를 지정해서 정렬하기](#명시적으로-key를-지정해서-정렬하기)  
  - [다중 기준 정렬을 하고 싶을 때](#1-다중-기준-정렬을-하고-싶을-때-기준이-2개-이상도-가능)  
  - [정렬 기준이 특정 필드나 계산된 값일 때](#2-정렬-기준이-특정-필드나-계산된-값일-때)  
  - [복잡한 기준을 설정하고 싶을 때](#3-복잡한-기준을-설정하고-싶을-때)
- [1. 1차원 배열 정렬](#1-1차원-배열-정렬)
- [2. 2차원 배열 정렬](#2-2차원-배열-정렬)
- [3. 2차원 상의 좌표들을 시계방향-or-반시계방향으로-정렬](#3-2차원-상의-좌표들을-시계방향-or-반시계방향으로-정렬)

## `sort()` 🆚 `sorted()`

| 항목         | `sort()`                      | `sorted()`                                                       |
|------------|-------------------------------|------------------------------------------------------------------|
| **적용 대상**  | 리스트 전용 (`list` 객체의 메서드)       | 모든 반복 가능한(iterable) 객체 (`list`, `tuple`, `set`, `dict`, `str` 등) |
| **리턴 값**   | `None` 반환 (리스트를 **제자리에서 정렬**) | 새로운 정렬된 리스트를 반환                                                  |
| **원본 변화**  | **원본 리스트가 변경됨**               | **원본은 그대로, 정렬된 복사본을 만듦**                                         |
| **가독성/용도** | in-place 정렬이 필요할 때            | 정렬 결과를 따로 보존하거나 임시 사용 시                                          |

## 명시적으로 key를 지정해서 정렬하기

```python
arr = [(2, 3), (1, 5), (2, 1), (1, 4)]
arr.sort(key=lambda x: (x[0], x[1]), reverse=True)
```

### 1. 다중 기준 정렬을 하고 싶을 때 (기준이 2개 이상도 가능)

ex. **내림차순, 오름차순 섞어서 하는것도 가능하다!!!!!**

```python
data = [
    (1, 2, 3),
    (1, 1, 5),
    (1, 1, 2),
    (2, 0, 0),
    (1, 2, 1)
]

# 1순위: 첫 번째 요소, 2순위: 두 번째 요소, 3순위: 세 번째 요소
data.sort(key=lambda x: (x[0], x[1], x[2]))
# 결과: [(1, 1, 2), (1, 1, 5), (1, 2, 1), (1, 2, 3), (2, 0, 0)]

# 1순위: 첫 요소 (내림차순), 2순위: 두 번째 요소 (오름차순), 3순위: 세 번째 요소 (내림차순)
data.sort(key=lambda x: (-x[0], x[1], -x[2]))
```

### 2. 정렬 기준이 특정 필드나 계산된 값일 때

ex. 정렬하고자 하는 리스트가 객체나 딕셔너리인 경우

```python
students = [{'name': 'Alice', 'score': 90},
            {'name': 'Bob', 'score': 85},
            {'name': 'Charlie', 'score': 95}]

# 점수(score) 기준 오름차순 정렬
students.sort(key=lambda s: s['score'])
```

### 3. 복잡한 기준을 설정하고 싶을 때

ex. 문자들을 길이 기준으로 정렬하고 싶을 때

```python
words = ['apple', 'kiwi', 'banana', 'fig']
words.sort(key=len)
# 결과: ['fig', 'kiwi', 'apple', 'banana']
```

ex. 모든 값을 절댓값으로 변환하여 절댓값을 기준으로 변환하고 싶을 때

```python
nums = [-10, 5, -2, 3]
nums.sort(key=lambda x: abs(x))
# 결과: [3, -2, 5, -10]
```

## 1. 1차원 배열 정렬

- 오름차순 정렬 : `arr.sort()`

  ```python
  arr = [3, 1, 4, 2]
  arr.sort()
  # 결과: [1, 2, 3, 4]
  ```  

- 내림차순 정렬 : `arr.sort(reverse=True)`
  ```python
  arr = [3, 1, 4, 2]
  arr.sort(reverse=True)
  # 결과: [4, 3, 2, 1]
  ```  

## 2. 2차원 배열 정렬

- 1순위 : 0번째 인덱스, 2순위 : 1번째 인덱스, ... 으로 오름차순 정렬
  ```python
  arr = [(2, 3), (1, 5), (2, 1), (1, 4)]
  arr.sort()
  # 결과: [(1, 4), (1, 5), (2, 1), (2, 3)]
  ```  
- 1순위 : 0번째 인덱스, 2순위 : 1번째 인덱스, ... 으로 내림차순 정렬
  ```python
  arr = [(2, 3), (1, 5), (2, 1), (1, 4)]
  arr.sort(reverse=True)
  # 결과: [(2, 3), (2, 1), (1, 5), (1, 4)]
  ```  
  명시적으로 key를 지정해 줄 수도 있다.
  ```python
  arr = [(2, 3), (1, 5), (2, 1), (1, 4)]
  arr.sort(key=lambda x: (x[0], x[1]), reverse=True)
  ```

## 3. 2차원 상의 좌표들을 시계방향 or 반시계방향으로 정렬

> 신발끈 공식에서 필요
>

- 기본 원리: 좌표들의 **중심점을 기준으로 각도를 계산한 후 정렬**
- 주의사항
  • 정렬 전 점들은 다각형 외곽 순서대로 주어져 있지 않을 수 있음
  • 이 정렬은 단순 다각형에만 적용 가능 (자기 자신을 교차하지 않는 도형)

- 반시계방향 정렬 (신발끈 공식에 일반적으로 사용)
  ```python
  import math

  def sort_points_ccw(points):
      cx = sum(x for x, y in points) / len(points)
      cy = sum(y for x, y in points) / len(points)
      return sorted(points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
  ```

- 시계방향 정렬
  ```python
  import math

  def sort_points_cw(points):
    cx = sum(x for x, y in points) / len(points)
    cy = sum(y for x, y in points) / len(points)
    return sorted(points, key=lambda p: -math.atan2(p[1] - cy, p[0] - cx))
  ```