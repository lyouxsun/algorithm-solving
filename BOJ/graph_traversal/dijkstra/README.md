## 다익스트라 알고리즘
1. **인접 행렬 & 힙(우선순위 큐) 사용**
2. **visited 배열 필요X, 힙이 빌 때 까지만 탐색하면 된다.**

- 알고리즘 분류
  - 간선의 가중치가 모두 양수일 때 (가중치가 모두 동일할 때에는 BFS)
  - 특정 노드에서 모든 노드로의 최단 경로를 구할 때
  - 시간 복잡도 = `O((V+E) log V)`

```python
from heapq import *
INF = float("inf")

def dijkstra(start):
    # 1. 초기화 작업
    dp = [INF for _ in range(V + 1)]
    dp[start] = 0
    q = []
    heappush(q, (0, start))

    # 2. s 에서 모든 노드까지의 최단경로 구하기 (dp 갱신하기)
    while q:  # 힙이 비면 종료
        dist, now = heappop(q)              # dist : s부터 now 까지의 최단경로
        for (end, cost) in graph[now]:      # cost : now부터 end 까지의 간선 비용
            if dp[end] > dist + cost:
                dp[end] = dist + cost
                heappush(q, (dp[end], end))
    return dp
```
> 더 자세한 코드를 보고 싶으면 [BOJ_14938](./BOJ_14938.py) 파일 확인 
