'''
Task:- 
Kefa decided to make some money doing business on the Internet for exactly n days. He knows that on the i-th day (1 ≤ i ≤ n) he makes ai money. Kefa loves progress, that's why he wants to know the length of the maximum non-decreasing subsegment in sequence ai. Let us remind you that the subsegment of the sequence is its continuous fragment. A subsegment of numbers is called non-decreasing if all numbers in it follow in the non-decreasing order.
Help Kefa cope with this task!
'''

'''
Input:- 
The first line contains integer n (1 ≤ n ≤ 10^5).
The second line contains n integers a1,a2,...,an (1 ≤ ai ≤ 10^9).
'''

'''
Output:- 
Print a single integer — the length of the maximum non-decreasing subsegment of sequence a.
'''

'''
Examples:- 
input
6
2 2 1 3 4 1
output
3

input
3
2 2 9
output
3
'''

input();c=m=s=0
for i in map(int,input().split()):c=[c+1,1][i<s];m=max(m,c);s=i
print(m)