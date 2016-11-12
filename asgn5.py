infile = open('one.txt','r')
intext = infile.read()
intext2 = intext.lower()
words = intext2.split()

#print(words)

def choose(ax,bx,prev):
	#choose = ""
	if ax==False and bx==False:
		return 1
	else:
		if ax==False and bx!=False:
			#print("it came here_1!")
			return 2
		elif ax!=False and bx==False:
			#print("it came here_2!")
			return 1
		else:
			#print("came here again!")
			if ax>=prev and bx>=prev:
				if ax<bx:
					return 1
				else:
					return 2
			elif ax<prev and bx<prev:
				if ax<bx:
					return 1
				else:
					return 2
			elif ax>=prev:
				return 1
			elif bx>=prev:
				return 2
			else:
				print("dumbass!")
	print("chosen",choose)


def onesort(lx,ly,prevx,prevlist):	
	count = 0
	while lx[0]!=False or ly[0]!=False:
		nx = choose(lx[0],ly[0],prevx)
		if nx==1:
			selected = lx.pop(0)
		elif nx==2:
			selected = ly.pop(0)
		#print(selected,"selected!")
		if count==0:
			lx.append(selected)
			#print(selected,"moved to listA")
			prevlist = 'a'
		else:
			if selected >= prevx:
				if prevlist=='a':
					lx.append(selected)
					#print(selected,"moved to listA")
					prevlist = 'a'
				else:
					ly.append(selected)
					#print(selected,"moved to listB")
					prevlist = 'b'
			else:
				if prevlist=='a':
					ly.append(selected)
					#print(selected,"moved to listB")
					prevlist = 'b'
				else:
					lx.append(selected)
					#print(selected,"moved to listA")
					prevlist = 'a'
		prevx = selected
		count = count+1
	#print('lx',lx)
	#print('ly',ly)
	return(lx,ly)

def writeitup(xlx):
	count = 0
	thiswordcount = 0
	prevword = ""
	thiswordcount = 1
	for k in range(len(xlx)+1):
		if k!=len(xlx)+1:
			if xlx[k]!=xlx[k-1]:
				print(xlx[k-1],thiswordcount)
			else:
				thiswordcount=thiswordcount+1
		else:
			print(xlx[len(xlx)+1],1)
	
def process():
	infile = open('one.txt','r')
	intext = infile.read()
	intext2 = intext.lower()
	alx = intext2.split()
	alx.append(False)
	aly = [False]
	while True:
		alx,aly=onesort(alx,aly,'z'*10,'a')
		#print(alx)
		#print(aly)
		if (len(alx)==1 or len(aly)==1)and alx[0]==False and aly[0]==False:
			break;
		else:
			alx.append(alx.pop(0))
			aly.append(aly.pop(0))
	#print(alx)
	writeitup(alx[1:])

if __name__=="__main__":
	process()
