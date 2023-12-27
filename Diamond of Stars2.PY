"""

Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5



The dots represent spaces.



Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *

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

incr_num = (n+1)//2

for i in range(1, incr_num + 1):
    p = 0
    for j in range(1,n+1):
        if j > (incr_num - i) and p < ((2*i)-1):
            print('*', end='')
            p = p + 1
        else:
            print(' ', end = '')
    print()

for i in range(incr_num, 1, -1):
    p = 1
    for j in range(1,incr_num+1):
        if j > (incr_num - i + 1):
            print('*', end='')
            p = p + 1
        else:
            print(' ', end = '')
    for k in range(1,p-1):
        print('*', end = '')
    print()