"""

Print the following pattern for the given number of rows.
Pattern for N = 4
1111
000
11
0
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
11111
0000
111
00
1


"""

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

a = 0

for i in range(1, n+1):
    if a == 0:
        a = 1
    else:
        a = 0
    for j in range(n-i+1, 0, -1):
        print(a, end = '')
    print()
