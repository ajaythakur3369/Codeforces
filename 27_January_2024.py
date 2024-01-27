'''
Task:-
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.
'''

'''
Input:- 
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 10^3.
'''

'''
Output:- 
Output the given word after capitalization.
'''

'''
Examples:- 
input: 
ApPLe
output: 
ApPLe

input: 
konjac
output: 
Konjac
'''

a = input()
b = list(a)
b[0] = b[0].upper()
print("".join(b))