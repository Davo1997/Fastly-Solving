def power(a:float, n:int):
    """This is a function that counts the inserted power of inserted
    number very very fastly ! (for ex. number^1.000.000).
    If you enter more than 1.000.000 (for ex. 10.000.000) - it raises 'inf'..."""

    assert n >= 0, "Please enter the 'power' as equal or more than ZERO !"
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(a, n - 1) * a
    elif n % 2 == 0:
        return power(a * a, n // 2)

print(power(2, 1000000))


def fac(n):
    """This is a function for fastly counting factorial of any
    number (up to 100.000 and more (works in 5-10 seconds)) without
    recursion, with list - values in it"""

    f = [1] * (n + 1)
    for i in range(1, n + 1):
        f[i] = f[i - 1] * i
    return f[n]

print(fac(100000))