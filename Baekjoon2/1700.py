N, K = map(int, input().split())
elecs = list(map(int, input().split()))

plugs = []

unPlugCount = 0

for eIdx, elec in enumerate(elecs):
    if elec in plugs:
        continue
    if len(plugs) < N:
        plugs.append(elec)
        continue

    farthestIdx = -1
    replacePlug = None
    for plug in plugs:
        nextUse = float("inf")

        if plug in elecs[eIdx + 1 :]:
            nextUse = elecs[eIdx + 1 :].index(plug)

        if nextUse > farthestIdx:
            farthestIdx = nextUse
            replacePlug = plug

    plugs[plugs.index(replacePlug)] = elec
    unPlugCount += 1

print(unPlugCount)
