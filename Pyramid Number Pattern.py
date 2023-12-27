"""
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
        1
      212
    32123
  4321234
543212345

"""

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

i = 1

while i <= n:
    j = 1
    while j <= (n):
        if j > n - i:
            print(n-j+1, end = '')
        else:
            print(' ', end = '')
        j = j + 1
    p = n  -j + 3
    while p <= i:
        print(p, end = '')
        p = p + 1
    i = i + 1
    print()