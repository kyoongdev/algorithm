## 문제 풀이

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
