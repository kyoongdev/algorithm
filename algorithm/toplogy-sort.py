n, m = map(int, input().split())
indegree = [0] * (n + 1)  # 진입차수에 대한 정보를 담은 배열을 생성한다.
# 데이터가 1부터 시작하기 때문에 n+1개를 생성했다.
# 각각의 인덱스는 노드의 숫자에 해당하고 인덱스의 값은 진입차수의 개수를 의미한다.

graph = [[] for _ in range(n + 1)]  # 각 노드별로 나가는 간선의 위치를 저장한다.
# 각 인덱스는 노드의 숫자에 해당하고 인덱스의 값에 해당하는 배열으로 간선이 이어진다는 것을 의미한다.
# 아래의 반복문을 통해 채워질 것이다.

queue = []  # 진입차수가 없는 노드가 들어갈 queue 자료구조이다.
result = []  # queue에서 빠져나온 순서대로 값이 들어갈 것이며, 이것이 정렬의 결과물이다.

for _ in range(m):
    prev, post = map(int, input().split())  # prev는 선행과목, post는 후수과목에 해당한다.
    graph[prev].append(post)  # graph의 prev인덱스에 해당하는 배열에 post를 추가한다. 즉, prev라는 과목이 수강되어야 post를 수강할 수 있다.
    indegree[post] += 1  # post의 선수과목이 지정되었으므로 진입차수를 1 추가한다.

for i in range(1, n + 1):  # 처음에는 먼저 진입차수가 0인 노드부터 찾습니다.
    if indegree[i] == 0:
        queue.append(i)


while queue:  # queue가 비게 된다면, 정렬이 모두 끝납니다. 그래프 내에 사이클이 존재한다면, queue 가 비지 않게 되고 무한루프를 돕니다.
    value = queue.pop(0)  # queue에서 값을 꺼냅니다.
    result.append(value)  # 결과값으로 저장합니다.
    for i in graph[value]:  # queue에서 꺼내진 값의 다음 노드로 연결된 노드들을 찾습니다.
        indegree[i] -= 1  # queue에서 꺼내진 값에서 나오는 진출간선을 없애줍니다.
        if indegree[i] == 0:  # 이후 진입차수가 0이 된 노드를 찾고
            queue.append(i)  # 해당 노드를 queue에 넣고 queue가 빌 때까지 위의 내용들을 반복합니다.

print(result)
