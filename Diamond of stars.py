"""from os import *
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

n = (n+1)//2
i = 1

while i <= n:
    j = 1
    p = 1
    while j <= n:
        if j >= n-i+1:
            print('*', end = '')
            p = p + 1
        else:
            print(' ', end = '')
        j = j + 1
        
        while p - 2 >= 1:
            print('*', end = '')
            p = p - 1
    i = i + 1
    print()

    
i = i - 2

while i >= 1:
    j = 1
    p = 1
    while j <= n:
        if j >= n-i+1:
            print('*', end = '')
            p = p + 1
        else:
            print(' ', end = '')
        j = j + 1
        
        while p - 2 >= 1:
            print('*', end = '')
            p = p - 1
    i = i - 1
    print()
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

n = (n+1)//2
i = 1

while i <= n:
    j = 1
    p = 1
    while j <= n:
        if j >= n-i+1:
            print('*', end = '')
            p = p + 1
        else:
            print(' ', end = '')
        j = j + 1
        
        while p - 2 >= 1:
            print('*', end = '')
            p = p - 1
    i = i + 1
    print()

    
i = i - 2

while i >= 1:
    j = 1
    p = 1
    while j <= n:
        if j >= n-i+1:
            print('*', end = '')
            p = p + 1
        else:
            print(' ', end = '')
        j = j + 1
        
        while p - 2 >= 1:
            print('*', end = '')
            p = p - 1
    i = i - 1
    print()