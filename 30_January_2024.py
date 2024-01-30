'''
Task:- 
There are n stones on the table in a row, each of them can be red, green or blue. Count the minimum number of stones to take from the table so that any two neighboring stones had different colors. Stones in a row are considered neighboring if there are no other stones between them.
'''

'''
Input:- 
The first line contains integer n (1≤n≤50) — the number of stones on the table.
The next line contains string s, which represents the colors of the stones. We'll consider the stones in the row numbered from 1 to n from left to right. Then the i-th character s equals "R", if the i-th stone is red, "G", if it's green and "B", if it's blue.
'''

'''
Output:- 
Print a single integer — the answer to the problem.
'''

'''
Examples:- 
input: 
3
RRG
output: 
1  

input: 
5
RRRRR
output: 
4 

input:  
4
BRBG

output:
0 
'''

num_of_stones = eval(input())
stones_clr = input()
min_stones = 0
 
for i in range(num_of_stones-1):
    if stones_clr[i] == stones_clr[i+1]:
        min_stones += 1
 
print(min_stones)