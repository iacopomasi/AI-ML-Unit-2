from math import floor

def median(l:list) -> float:
    l = sorted(l)
    length = len(l)
    if (length % 2 == 0):
        a = l[(length // 2) - 1]
        b = l[length // 2]
        return (a + b) / 2
    return l[floor(length) // 2]

def arithmetic_mean(obs:list) -> float:
    return sum(obs) / len(obs)

def pearson_correlation_coefficient(X : list, Y : list) -> float:
    meanX = arithmetic_mean(X, len(X))
    meanY = arithmetic_mean(Y, len(Y))

    std_devX = sum([(x - meanX)**2 for x in X])
    std_devY = sum([(y - meanY)**2 for y in Y])

    prod_std_devXY = (std_devX * std_devY) ** (1/2)

    # We are assuming that the length of the two vectors X and Y is equal
    res = 0
    for i in range(len(X)):
        res += a[i] * b[i]
    res = res / prod_std_devXY
    return res
