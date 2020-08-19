def print_max(a, n, k):
    max_upto = [0 for i in range(n)]
    s = []
    s.append(0)

    for i in range(1, n):
        while (len(s) > 0 and a[s[-1]] < a[i]):
            max_upto[s[-1]] = i - 1
            del s[-1]

        s.append(i)

    while (len(s) > 0):
        max_upto[s[-1]] = n - 1
        del s[-1]

    j = 0
    for i in range(n - k + 1):
        while (j < i or max_upto[j] < i + k - 1):
            j += 1
        print(a[j], end=" ")
    print()


num = int(input("Enter number of elements: "))
a = []
for i in range(num):
    char = int(input())
    a.append(char)

n = len(a)
k = int(input("Enter length of window: "))
print_max(a, n, k)
