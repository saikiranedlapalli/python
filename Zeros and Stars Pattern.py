"""
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000

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
    k = i
    star_cnt = 0
    while j <= ((2*n)+1):
        if (j == i or j == k) and (star_cnt < 3):
            print('*', end = '')
            star_cnt = star_cnt + 1
            k = k + (n - i + 1)
        else:
            print(0, end = '')
        j = j + 1
    i = i + 1
    print()