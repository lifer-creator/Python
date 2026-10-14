def fib_list(n):
    """前 n 个斐波那契数；n <= 0 时返回 []"""
    if n <= 0:
        return []
    fibs = [1]
    while len(fibs) < n:
        if len(fibs) == 1:
            fibs.append(1)
        else:
            fibs.append(fibs[-1] + fibs[-2])
    return fibs


def dedupe(nums):
    """去重，保持第一次出现的顺序；不改动原列表"""
    result = []
    for x in nums:
        if x not in result:
            result.append(x)
    return result


def is_prime(x):
    """判断单个数字是不是素数"""
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def primes_up_to(n):
    """n 以内（含 n）的所有素数组成的列表"""
    primes = []
    for x in range(2, n + 1):
        if is_prime(x):
            primes.append(x)
    return primes


if __name__ == "__main__":
    print("fib_list(7)      =", fib_list(7))
    print("fib_list(1)      =", fib_list(1))
    print("fib_list(0)      =", fib_list(0))
    print("dedupe(...)      =", dedupe([1, 2, 2, 3, 1]))
    print("primes_up_to(30) =", primes_up_to(30))
    print("primes_up_to(1)  =", primes_up_to(1))
