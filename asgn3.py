import random
import math

#my solution for assignment3

def weighted_random(wt):
	r = random.random()
	if r<=wt:
		return 1
	else:
		return -1
	
def onerandomwalk(start,left,right,max_steps,per_right):
	currstep = start
	for k in range(max_steps):
		numx = weighted_random(per_right)
		currstep = currstep + numx
		if currstep==left:
			#print("stopped left!")
			return -(k+1)
		elif currstep==right:
			#print("stopped right!")
			return k+1
		else:
			continue
	return max_steps

def standard_dev(listx):
	sumx = sum(listx)
	nums = len(listx)
	avgx = sumx/nums
	sumofsq = 0
	for k in range(nums):
		sumofsq += (listx[k]-avgx)*(listx[k]-avgx)
	avx = sumofsq/nums
	resx = math.sqrt(avx)
	return nums,avgx,resx
	
def lol():
	'''
	startpos = int(input("Where do you want to start?"))
	minpos = int(input("Enter the minimum value"))
	maxpos = int(input("Enter the maximum value"))
	maxsteps = int(input("Enter the maximum number of steps!"))
	howmany = int(input("How many times do you want to iterate?"))
	whatright = int(input("What is the percentage of moving right? Enter a number 1-100"))
	wr = float(whatright)/100
	'''
	#hardcoded
	startpos = 200
	minpos = 100
	maxpos = 300
	maxsteps = 5000
	howmany = 1000
	wr = 0.51
	
	listone = []
	listleft = []
	listright = []
	for j in range(howmany):
		res = onerandomwalk(startpos,minpos,maxpos,maxsteps,wr)
		#print("steps =", res)
		if res==maxsteps:
			listone.append(res)
		elif res>0:
			listright.append(res)
		elif res<0:
			listleft.append(-res)
		else:
			print("we have a problem!")
	#print(listone)
	#print(listleft)
	#print(listright)
	listall = []
	listall.extend(listone)
	listall.extend(listleft)
	listall.extend(listright)
	print(standard_dev(listone))
	print(standard_dev(listleft))
	print(standard_dev(listright))
	print(standard_dev(listall))
	#print(standard_dev([1,2,3,4,5]))

def main():
	for k in range(1):
		lol()
	
if __name__=="__main__":
	main()
