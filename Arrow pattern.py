"""
Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.
Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
11
Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*

"""

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

i = 1

while i <= (n+1)/2:
    j = 1
    p = 1
    while j <= i:
        if j == i:
            print('* ', end = '')
        else:
            print(' ', end = '')
        j = j + 1
    while p < i:
        print('* ', end = '')
        p = p + 1
    i = i + 1
    print()

i = i - 2
while i > 0:
    j = 1
    p = 1
    while j <= i:
        if j == i:
            print('* ', end = '')
        else:
            print(' ', end = '')
        j = j + 1
    while p < i:
        print('* ', end = '')
        p = p + 1
    i = i - 1
    print()