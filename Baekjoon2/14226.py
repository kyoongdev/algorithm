from collections import deque

S = int(input())

queue = deque([(1, 0, 0)])  # (현재 화면 이모티콘 수, 클립보드 이모티콘 수, 작업 시간)
visited = set()  # (화면 이모티콘 수, 클립보드 이모티콘 수)
visited.add((1, 0))

while queue:
    imos, clip, count = queue.popleft()

    # 목표 상태 도달
    if imos == S:
        print(count)
        break

    # 화면에 있는 이모티콘을 클립보드에 복사
    if (imos, imos) not in visited:
        visited.add((imos, imos))
        queue.append((imos, imos, count + 1))

    # 클립보드의 이모티콘을 화면에 붙여넣기
    if clip > 0 and (imos + clip, clip) not in visited:
        visited.add((imos + clip, clip))
        queue.append((imos + clip, clip, count + 1))

    # 화면에서 이모티콘 하나 삭제
    if imos > 0 and (imos - 1, clip) not in visited:
        visited.add((imos - 1, clip))
        queue.append((imos - 1, clip, count + 1))
