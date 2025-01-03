N = int(input())
signal = input()
"""
0 : .
1 : #

###.. : 11100


"""


length = len(signal) // 5
signals = []
for i in range(5):
    signals.append(signal[i * length : (i * length) + length])


number_hash = {
    "####.##.##.####": "0",
    "#####": "1",
    "###..#####..###": "2",
    "###..####..####": "3",
    "#.##.####..#..#": "4",
    "####..###..####": "5",
    "####..####.####": "6",
    "###..#..#..#..#": "7",
    "####.#####.####": "8",
    "####.####..####": "9",
}


idx = 0
answers = []

while idx < length:
    if signals[0][idx] == ".":
        idx += 1
        continue

    # 1인 경우
    if all(signals[row][idx] == "#" for row in range(5)) and (
        idx + 1 >= length or signals[0][idx + 1] == "."
    ):

        answers.append("1")
        idx += 1
        continue

    # 나머지 숫자
    targets = ["".join(signals[row][idx : idx + 3]) for row in range(5)]
    target = "".join(targets)
    answers.append(number_hash[target])
    idx += 3


print("".join(answers))
