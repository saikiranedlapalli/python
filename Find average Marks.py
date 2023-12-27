""""

Question:

Write a program to input marks of three tests of a student (all integers). Then calculate and print the average of all test marks.
Input format :
3 Test marks (in different lines)
Output format :
Average 
Sample Input 1 :
3 
4 
6
Sample Output 1 :
4.333333333333333
Sample Input 2 :
5 
10 
5
Sample Output 2 :
6.666666666666667

"""

# Read input as sepcified in the question
# Print output as specified in the question
sub1_marks = int(input())
sub2_marks = int(input())
sub3_marks = int(input())

avg_marks = (sub1_marks + sub2_marks + sub3_marks)/3
print(avg_marks)