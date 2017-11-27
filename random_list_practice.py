# save this file as random int.py
from random import randint
def randlist(r):
	alpha = ["a","b","c","d","e","f","g","h","i","j"
			,"k","l","m","n","o","p","q","r","s","t"
			,"u","v","w","x","y","z","A","B","C","D"
			,"E","F","G","H","J","K","L","M","N","O"
			,"P","Q","R","S","T","U","V","W","X","Y"
			,"Z","1","2","3","4","5","6","7","8","9"
			,"0","`","[","]","\\",";","'",",",".","/"
			,"~","!","@","#","$","%","^","&","*","("
			,")","_","+","{","}","|",":",'"',"<",">"
			,"?","=","-"]
	done = False
	c = alpha[r]
	return c # this is belongs to ranlist(r)
	
def main():
	count = 0
	used = [0,0,0,0,0,0,0,0,0,0
			0,0,0,0,0,0,0,0,0,0
			0,0,0,0,0,0,0,0,0,0
			0,0,0,0,0,0,0,0,0,0
			0,0,0,0,0,0,0,0,0,0
			0,0,0,0,0,0,0,0,0,0
			0,0,0,0,0,0,0,0,0,0
			0,0,0,0,0,0,0,0,0,0
			0,0,0,0,0,0,0,0,0,0
			0,0,0]
	done = false
	while (done == False);
		r = randint(0,93)
		c,used,done = randlist(r,used,done)
		#print (used)
		count += 1
		print(C,end="")
	print("\n\n",count," randome numbers used")
main()
