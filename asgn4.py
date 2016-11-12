import math

def char2num(chrx):
	return ord(chrx)-65

def num2char(numx):
	return chr(numx+65)
	
def checkbanned(chrx):
	z=ord(chrx)-65
	if(z>0 and z<26):
		return 0
	else:
		return 1

def keylong(key,lenx):
	len1 = len(key)
	b = lenx%len1
	#print('b=',b)
	keyx = ""
	d = math.floor(lenx/len1)
	#print("d=",d)
	for j in range(d):
		keyx = keyx+key
	keyx=keyx+key[:b]
	return keyx

def sumitup(chr1,chr2):
	x = (char2num(chr1)+char2num(chr2))%26
	#print('x=',x)
	return num2char(x)

def diffitup(chr1,chr2):
	x = (char2num(chr1)-char2num(chr2))%26
	#print('x=',x)
	return num2char(x)
	
def encrypt(message,key):
	newkey = keylong(key,len(message))
	resx = ""
	for j in range(len(message)):
	
		ax =sumitup(message[j],newkey[j])
		#print('ax',ax)
		resx=resx+ax
	return(resx)
	
def advancedencrypt(message,key):
	newkey = keylong(key,len(message))
	resx = ""
	bx = 0
	for j in range(len(message)):
		bbit = checkbanned(message[j])
		if(bbit==0):
			ax =sumitup(message[j],newkey[j-bx])
		else:
			ax=message[j]
			bx=bx+1
		print(bbit,message[j],newkey[j],ax)
		resx=resx+ax
	return(resx)

def decrypt(cryptcode,key):
	newkey = keylong(key,len(cryptcode))
	resx = ""
	for j in range(len(cryptcode)):
		ax =diffitup(cryptcode[j],newkey[j])
		resx=resx+ax
	return(resx)

def advanceddecrypt(cryptcode,key):
	newkey = keylong(key,len(cryptcode))
	resx = ""
	bx = 0
	for j in range(len(cryptcode)):
		bbit = checkbanned(cryptcode[j])
		#print(bbit,message[j],newkey[j])
		if bbit==0:
			ax = diffitup(cryptcode[j],newkey[j-bx])
		else:
			ax = cryptcode[j]
			bx=bx+1
		resx=resx+ax
	return(resx)
	
def main():
	mess = input("enter the message in CAPS!")
	keyy = input("enter the key in CAPS!")
	crypt = advancedencrypt(mess.upper(),keyy.upper())
	print("original  =",mess.upper())
	print("encrypted =",crypt)
	decr = advanceddecrypt(crypt,keyy.upper())
	print("decrypted =",decr)
	
if __name__=='__main__':
	main()