'''
Task:- 
For a positive integer n let's define a function f:

f(n) = -1+2-3+..+(-1)^n.n

Your task is to calculate f(n) for a given integer n.
'''

'''
Input:- 
The single line contains the positive integer n (1 ≤ n ≤ 10^15).
'''

'''
Output:- 
Print f(n) in a single line.
'''

'''
Examples:- 
input:
4
output:
4

input:
5 
output: 
-3 
'''

n=int(input())
print(n//2-n%2*n)