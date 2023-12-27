"""

Print the following pattern for the given number of rows.
Pattern for N = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
3
Sample Output :
33333
32223
32123
32223
33333

"""

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

for i in range(n):
    p = n
    for j in range(i+1):        
        print(p, end = '' )
        p = p - 1
    for k in range(2*(n - i - 1)):
        print(n - i, end = '')
    p = p + 2
    for m in range(i):
        print(p, end = '')
        p = p + 1
    print()
    
    
for i in range(n-1,0,-1):
    p = n
    for j in range(i):        
        print(p, end = '' )
        p = p - 1
    for k in range(1, 2*(n - i)):
        print(n - i + 1, end = '')
    for m in range(i):
        p = p + 1
        print(p, end = '')
    print()
