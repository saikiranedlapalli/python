"""

Print the following pattern for n number of rows.
Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1

"""

n = int(input())

i = 1


while i <= n:
    j = 1
    k = 1
    while j <= i:
        print(j, end = '')
        j = j + 1
        k = k + 1
    while k <= (2*n):
        if k > (2*n) - i:
            print( (2*n) - k + 1, end = '')
        else:
            print(' ', end = '')
        k = k + 1
    i = i + 1
    print()