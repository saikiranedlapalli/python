"""
Print the following pattern for the given N number of rows.
Pattern for N = 4




The dots represent spaces.


Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
3
Sample Output 1:
      1 
    12
  123
Sample Input 2:
4
Sample Output 2:
      1 
    12
  123
1234

"""

## Read input as specified in the question
## Print the required output in given format
n = int(input())

i = 1

while i <= n:
    j = 1
    p = 1
    while j <= n:
        if j >= (n - i + 1):
            print(p, end = '')
            p = p + 1
        else:
            print(' ', end = '')
        j = j + 1
    i = i + 1
    print()