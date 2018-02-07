from random import randint
import random as rand
import sys
import numpy
def dp(startx,starty,endx,endy):
	num1=0
	num2=0
	if startx<endx:
		num1=dp(startx+1,starty,endx,endy)
	if starty<endy:
		num2=dp(startx,starty+1,endx,endy)
	return max(point[startx,starty]+num1,point[startx,starty]+num2)
for u in range(1,11):
	print 'Level [',u,'/10 ]'
	l=rand.sample(range(2, 60), 2)
	n=l[0]
	m=l[1]
	point=numpy.zeros((n+1, m+1))
	checkpoint=numpy.zeros(m+1) 
	print n,m,
	for i in range(1,n+1):
		for j in range(1,m+1):
			point[i,j]=randint(1,100)
	num=randint(1,n-1)
	check1=rand.sample(range(1, n),num )
	check1.sort()
	check1=list(check1)
	check2=list([rand.randrange(1,m) for i in range(num)])
	check2.sort()
	checkpoint=zip(check1,check2)
	checkpoint.append((n,m))
	count=0
	count1=0
	for i in point:
		count1=0
		for j in i:
			if count!=0 and count1!=0:
				print int(j),
			count1=count1+1
		count=count+1
		print ''
	for i in checkpoint:
		for j in i:
			print j,
		print ''
	initptx=1
	initpty=1
	sum=0

	for i in checkpoint:
		sum+=dp(initptx,initpty,i[0],i[1])-point[i[0],i[1]]
		initptx=i[0]
		initpty=i[1]
	sum+=point[n,m]
	sum=int(sum)
	print sum
	ans=input()
	if ans!=sum:
		print 'Wrong answer , no flag here!!'
		exit(0)
print 'Congrats the flag is blah blah'
