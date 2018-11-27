#sets_3.py okb
alpha = {"a","b","c","d","e","f"}
bravo = {"z","y","x","w","v"}
charlie = alpha.union(bravo)
for x in charlie:
	print(x," ",end="c")
print("pop 1")
thepop = charlie.pop()
print (thepop)
print("pop 2")
thepop = charlie.pop()
print (thepop)
"""
The union method combines two sets.
The concept of "pop" is an important
function in data stuctures that resemble
a stack.
A stack is a list where data 
moves first in the last out.
"""
