from collections import defaultdict
from collections import deque

# 한 폴더 안에 같은 파일 2개 이상 X

N, M = list(map(int, input().split()))


files = []
for _ in range(N + M):
    tmp = input().split()

    p, f, c = tmp
    files.append((p, f, c))

Q = int(input())

quries = []
for _ in range(Q):
    quries.append(input())

# 쿼리 순서대로 한 줄씩 폴더 하위에 있는 파일의 종류와 개수와 파일의 총 개수 출력
# c == 1 폴더, c == 0 파일
fileDict = defaultdict(dict)
"""
main :{
  folders: [],
  files : []
,
FolderA : {
  parent : "main",
  folders: [],
  files : []

}
}
"""
for parent, f, c in files:
    if parent not in fileDict:
        fileDict[parent]["folders"] = []
        fileDict[parent]["files"] = []
        fileDict[parent]["parent"] = ""
    for key, value in fileDict.items():
        if parent in value["folders"]:
            fileDict[parent]["parent"] = key

    if c == "0":
        fileDict[parent]["files"].append(f)
    else:
        fileDict[parent]["folders"].append(f)
# print(fileDict)

answers = []
for query in quries:
    query = deque([query.split("/")[-1]])
    files = []

    while query:
        folder = query.popleft()
        if (
            folder in fileDict.keys()
            and "folders" in fileDict[folder]
            and "files" in fileDict[folder]
        ):
            target = fileDict[folder].copy()

            files.extend(target["files"].copy())
            folders = deque(target["folders"].copy())

            while folders:
                f = folders.popleft()

                if "folders" in fileDict[f] and len(fileDict[f]["folders"]) > 0:
                    folders.extend(fileDict[f]["folders"].copy())
                if "files" in fileDict[f]:
                    files.extend(fileDict[f]["files"].copy())

    answers.append((len(set(files)), len(files)))

for x, y in answers:
    print(x, y)
