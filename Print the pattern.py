"""
Print the following pattern for the given number of rows.
Pattern for N = 5
 1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
4
Sample Output :
 1  2  3  4
 9 10 11 12
13 14 15 16
 5  6  7  8

"""

n = int(input())

mid_num = (n+1)//2
lines_printed = 0
for i in range(mid_num):
    for j in range(1, n+1):
        print((i*n*2)+j, end = ' ')
        p = i*n*2+1
    print()
    lines_printed = lines_printed + 1

if n%2 == 0:
    for j in range(0, n):
        print(p + n + j, end = ' ')
    print()
    p = p + n
else:
    for j in range(n):
        print(p - n + j, end = ' ')
    print()
    p = p - n
lines_printed = lines_printed + 1

for m in range(lines_printed, n):
    for x in range(0,n):
        print(p - (2*n) + x, end = ' ')
    print()
    p = p - (2*n)