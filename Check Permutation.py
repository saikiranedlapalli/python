'''
Check Permutation

For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
Permutations of each other
Two strings are said to be a permutation of each other when either of the string's characters can be rearranged so that it becomes identical to the other one.

Example: 
str1= "sinrtg" 
str2 = "string"

The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings are a permutation of each other.
Input Format:
The first line of input contains a string without any leading and trailing spaces, representing the first string 'str1'.

The second line of input contains a string without any leading and trailing spaces, representing the second string 'str2'.
Note:
All the characters in the input strings would be in lower case.
Output Format:
The only line of output prints either 'true' or 'false', denoting whether the two strings are a permutation of each other or not.

You are not required to print anything. It has already been taken care of. Just implement the function. 
Constraints:
0 <= N <= 10^6
Where N is the length of the input string.

Time Limit: 1 second
Sample Input 1:
abcde
baedc
Sample Output 1:
true
Sample Input 2:
abc
cbd
Sample Output 2:
false

Python (3.5)
1234567891011121314151617181920212223242526

from sys import stdin


def isPermutation(str1, str2) :
    #Your code goes here
    n1 = len(str1) 
    n2 = len(str2)
    if (n1 != n2):
    	return False


CUSTOM INPUT


SUBMIT SOLUTION


PREVIOUS


NEXT
''''


from sys import stdin


def isPermutation(str1, str2) :
    #Your code goes here
    n1 = len(str1) 
    n2 = len(str2)
    if (n1 != n2):
    	return False

    # Sort both strings 
    a = sorted(str1) 
    str1 = "".join(a) 
    b = sorted(str2) 
    str2 = "".join(b) 

    # Compare sorted strings 
    for i in range(0, n1, 1): 
    	if (str1[i] != str2[i]): 
    		return False

    return True


#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

