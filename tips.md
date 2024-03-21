## 문제 풀이

**좌표상 외각 경로**  
외각 경로를 따라다니는 경우 1x1에서 예외 케이스가 자주 발생  
=> 좌표 크기를 2배수로 늘리고 나누는게 빠름

**주어진 문제에 맞는 값을 미리 찾아두는 경우**

결과값에 대해 연산이 길어지거나 풀이가 복잡한 경우  
해당 결과값이 나올 수 있는 경우의 수를 미리 찾아두는 것이 방법이 될 수 있음

**엣지케이스 찾기**

1. 비어있거나 하나만 있는 케이스
2. 첫번째 혹은 마지막 케이스
3. 크기가 굉장히 큰 케이스
4. 범위가 굉장히 넓은 케이스
5. 양수만 있는, 혹은 음수만 있는 케이스
6. 배열 사이즈가 클 때 전체 반복을 두번 이상 하면 타임아웃에 걸릴 수 도 있다고 생각하자.
7. 같은 값이 들어가는 케이스

**DP문제**  
DP의 경우 어떤 조건에 어떤 값을 어떻게 저장할 것인가를 판별하는게 중요하다.
조건을 여러개 -> 다차원 배열

**데이터 수에 따른 최대 시간복잡도**  
|데이터수|최대 시간복잡도|  
|---|---|
|10^8|n,logN|
|10^6|nlogN|
|10^4|n^2|
|500|n^3|
|20|n!,2^n|

**탐색 dfs bfs 구별법**  
보통 벽(막혀있는 경우)의 개념이 들어가면 bfs가 유리

**bfs 주의사항**
밟을 수 있을 때만 visited 처리를 해야함

움직일 수 있는 경우의 수가 추가된다면 3차원으로 visited를 만드는 것도 고려해보자 (이때 중요한 점은 visited 체크할 대상은 다시 queue에 들어갈 것과 동일해야함)

**백트래킹**  
dfs 탐색 과정 중 반례로 인해 다시 이전 값으로 돌아가야할 때 사용
반드시 탈출 조건을 잘 명시해줘야함! (특히 결과 배열같은 거 사용할 때)

**2차원배열 누적합**
2차원 배열에서 (x1,y1)부터 (x2,y2)까지 n만큼의 변화는 (x1,y1)에 +n, (x1,y2+1)에 -n, (x2+1,y1)에 -n, (x2+1,y2+1)에 +n을 한 것과 같다.

**bfs와 dp 구별**
경로 문제에서 bfs를 쓸 지 dp를 쓸 지 헷갈린다면  
도착할 수 있는 모든 경우의 수를 구할 때는 dp, 도착할 수 있는 최소한의 거리(방법)이면 bfs를 선택해보자.

```python

def dfs(~~):
  if ~~ :## 탈출조건
    return
  for ~ in ~~:
    # 적용
    dfs()
    # 백트래킹 -> dfs가 종료되지 않으면 백트래킹으로 이전 상황으로 돌아감
```

## Python 내장 모듈

### 커스텀 Sorting

```python
from functools import cmp_to_key

def sort():
  ## sort

list1 = []
list1.sort(key=cmp_to_key(sort))
```

functools 내의 cmp_to_key를 통해 커스텀 sorting 가능

### Counter

```python
from collections import Counter
dict1 = {
  "a" : 1,
  "b" : 2
}

common = Count(dict1).most_common()
print(common) ## [('b',2),('a',1)]
```

collection 내부의 Counter를 통해 각 Dictionary Key의 빈도수를 찾을 수 있음

### 순열,중복순열,조합,중복조합

**순열**

```python
from itertools import permutations

sets = [1,2,3]

data = itertools.permutation(sets, 2)

for i in data:
   print(i)

#print
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
```

**중복순열**

```python
from itertools import product

sets = [1,2,3]

data = itertools.product(sets, repeat = 2)

for i in data:
   print(i)

#print
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)
```

**조합**

```python
from itertools import combinations

sets = ['A', 'B', 'C']

data = itertools.combinations(sets, 2)

for i in data:
   print(i)

#print
(A, B)
(A, C)
(B, C)
```

**중복조합**

```python
from itertools import combinationswith_replacement

sets = ['A', 'B', 'C']

data = itertools.combinations_with_replacement(sets, 2)

for i in data:
   print(i)

#print_
(A, A)
(A, B)
(A, C)
(B, B)
(B, C)
(C, C)
```

### 문자열

```python
ord("a") ## 97
char(97) ## a
```

```python
## 대소문자 변경
a =  "asdbASDBAS"
a.lower()
a.upper()

## 숫자여부
a.isdigit()
```

---

## 함수

### 배열의 회전

```python
## 시계방향으로 1번씩 회전
def rotated(target):
    n = len(target)
    m = len(target[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = target[i][j]

    return result

## 정규화를 통한 회전
def rotate(block):
  spin90,spin180,spin270 = set(),set(),set()

  while block:
    x,y = block.pop()
    spin90.add((y,-x))
    spin180.add((-x,-y))
    spin270.add((-y,x))

  return spin90,spin180,spin270
```

### 배열의 껍데기만 고르는 법

```python
loops = min(N, M) // 2
for i in range(loops):
    deq.clear()
    deq.extend(matrix[i][i:M-i])
    deq.extend([row[M-i-1] for row in matrix[i+1:N-i-1]])
    deq.extend(matrix[N-i-1][i:M-i][::-1])
    deq.extend([row[i] for row in matrix[i+1:N-i-1]][::-1])
```
