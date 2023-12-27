"""

Print the following pattern for a given n.
For eg. N = 6
123456
  23456
    3456
      456
        56
          6
        56
      456
    3456
  23456
123456
Sample Input 1 :
4
Sample Output 1 :
1234
  234
    34
      4
    34
  234
1234

"""

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if j < i:
            print(' ', end = '')
        else:
            print(j, end = '')
    print()


for i in range(i+1, 2*n):
    for j in range(1, n+1):
        if j < ((2*n) - i):
            print(' ', end = '')
        else:
            print(j, end = '')
    print()
