count = 0
N = 15
A = [0 for _ in range(N)]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def printSet(n):
    global count
    count += 1
    print("%d : "% (count), end="" )
    for i in range(n):
        if A[i] == 1:
            print('{} '.format(data[i]), end="")
    print()

def powerset(n, k):
    if n == k:
        printSet(n)
        # for i in range(N):
        #     if A[i] == 1:
        #         print(i+1, end=' ')
        # print()
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

powerset(N, 0)