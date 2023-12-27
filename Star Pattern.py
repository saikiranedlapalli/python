"""

Print the following pattern
Pattern for N = 4



The dots represent spaces.



Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1 :
3
Sample Output 1 :
   *
  *** 
 *****
Sample Input 2 :
4
Sample Output 2 :
    *
   *** 
  *****
 *******

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
    p = 1
    while j <= n:
        if j >= (n-i+1):
            print('*', end = '')
            p = p + 1
        else:
            print(' ', end = '')
        
        while p > 2:
            print('*', end = '')
            p = p - 1
        j = j + 1
    i = i + 1
    print()