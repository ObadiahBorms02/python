from random import randint
def randlist(r,done,usedlist):
		alpha = ["a","b","c","d","e","f"]
		usedlist[r] = 1
		c = alpha[r]
		sum = 0
		for i in range(len(usedlist)):
			sum = sum + usedlist[i]
	    # print (sum)
		return c, usedlist # this is belongs to ranlist(r)
	
	
def main():
		used = [0,0,0,0,0,0]
		done = False
		while True:
			r = randint(0,5) # make a randome number
			c = randlist(r,done,used)
			print (used)
			# print(c,end='')
			
main()


#http://www.youtube.com/watch?v=sugvnHA7ElY
#https://www.youtube.com/watch?v=Huz6bS0ulm4
#https://www.youtube.com/watch?v=JtKOP-ThcbU
#https://pythonprogramming.net/

# .format
#https://www.youtube.com/watch?v=vTX3IwquFkc


#python tcp
#http://www.youtube.com/watch?v=WrtebUkUssc
