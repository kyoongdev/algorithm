from itertools import combinations

H, W = map(int, input().split())
N = int(input())

stickers = []
for _ in range(N):
    stickers.append(list(map(int, input().split())))


stickerCombi = list(combinations(range(N), 2))

answer = 0


def check(ox, oy, tx, ty):

    if (ox + tx <= H and max(oy, ty) <= W) or (oy + ty <= W and max(ox, tx) <= H):
        return True

    if (ox + ty <= H and max(oy, tx) <= W) or (oy + tx <= W and max(ox, ty) <= H):
        return True

    if (oy + tx <= H and max(ox, ty) <= W) or (ox + ty <= W and max(oy, tx) <= H):
        return True

    if (oy + ty <= H and max(ox, tx) <= W) or (ox + tx <= W and max(oy, ty) <= H):
        return True

    return False


for one, two in stickerCombi:
    ox, oy = stickers[one]
    tx, ty = stickers[two]

    if check(ox, oy, tx, ty):

        answer = max(answer, ox * oy + tx * ty)

print(answer)
