primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, ]


def returnSolution(a, n, k, N):
    output = ""
    for i in range(k):
        if a[i] is not 0:
            output += str(a[i]) + "*" + str(primes[i]) + "+"
    output = output.rstrip("+")
    print(output + "\n")


def solution(a, n, k, N):
    sum = 0
    for i in range(k):
        sum += primes[i] * a[i]
    if sum == N:
        return True
    else:
        return False


def valid(a, n, k, N):
    sum = 0

    if k == n:
        return False

    for i in range(k):
        sum += primes[i] * a[i]

    if sum < N:
        return True
    else:
        return False


def bkt_r(a, n, k, N):
    if solution(a, n, k, N):
        returnSolution(a, n, k, N)
    else:
        for i in range(6):
            a[k] = i
            if valid(a, n, k, N):
                bkt_r(a, n, k + 1, N)


def bkt_i(a, n, k, N):
    k = 0
    a[k] = 0
    while k >= 0:
        if solution(a, n, k, N):
            returnSolution(a, n, k, N)
            k -= 1
        else:
            if a[k] < 5:
                a[k] += 1
                if valid(a, n, k, N):
                    k += 1
            else:
                a[k] = 0
                k -= 1

N = 12  # int(input("Number:"))

a = [0 for i in range(10)]
n = 6
k = 0

bkt_i(a, n, k, N)
