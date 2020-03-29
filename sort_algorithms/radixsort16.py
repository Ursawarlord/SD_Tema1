def radixSortHex(array):
    pos = 0
    n = len(array)
    result = [0] * n
    max = 1
    while max >> pos > 0:
        count = [0] * 16
        for each in array:
            if pos == 0:
                if each > max:
                    max = each
            count[(each >> pos) & 0xf] += 1
        for i in range(1, 16):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            current = (array[i] >> pos) & 0xf
            result[count[current] - 1] = array[i]
            count[current] -= 1
        for i in range(0, n):
            array[i] = result[i]
        pos += 4
