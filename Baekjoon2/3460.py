T = int(input())


def digit(n):
    binary = ""

    while n != 0:
        value = n % 2
        if value == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary

        n = n // 2
    return binary


for i in range(T):
    n = int(input())
    binary = digit(n)

    binary = binary[::-1]
    idxs = [str(idx) for idx, b in enumerate(binary) if b == "1"]
    print(" ".join(idxs))
