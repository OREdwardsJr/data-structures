def fibonacci(limit: int) -> list:
    res = [0, 1]
    l, r = 0, 1
    count = 0
    while count in range(limit):
        res.append(res[l] + res[r])
        l += 1
        r += 1
        count += 1

    return res


print(fibonacci(10))

print(13195 % 29)
