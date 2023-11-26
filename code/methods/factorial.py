def factorial_list(n: int) -> list[int]:
    """returns a list containing all factorials up to n!"""
    values = []
    last = 1
    for k in range(n + 1):
        v = k
        if v == 0:
            v = 1
        last = last * v
        values.append(last)

    return values


if __name__ == "__main__":
    for v in [0, 1, 2, 5, 10]:
        print("factorial of %d" % v)

        ll = factorial_list(v)
        for k in range(len(ll)):
            print("%2d) %d" % (k, ll[k]))
