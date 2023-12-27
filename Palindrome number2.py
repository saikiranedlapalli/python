"""
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
Sample Input 1 :
121
Sample Output 1 :
true
Sample Input 2 :
1032
Sample Output 2 :
false

"""

def checkPalindrome(num):
    rev_num = 0
    nbr = num
    while nbr > 0:
        reminder = nbr % 10
        rev_num = (rev_num  * 10) + reminder
        nbr = nbr // 10
    if num == rev_num:
        return True
    else:
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
