ffffffffffffffffff#binarystring.py
def bincon(decimal):
	print("BINARY")
	print(decimal)
	binstr=""
	for i in range (8):
		bin = decimal % 2
		binstr = binstr + str(bin)
		decimal = decimal // 2
		print (bin)
	print(binstr)
	print(binstr[::-1])

def main():
	print("INPUT A -1 TO EXIT THE LOOP")
	dec = ("INPUT AN INTEGER LESS THAN 256 AND GREATER THAN -1")
	done = 0;
	while (done >= 0):
		dec = input("INPUT AN INTEGER : ")
		bincon(dec)
main()
