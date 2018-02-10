from random import randint
import random as rand
from pythonds.basic.stack import Stack
import numpy
import sys
def Xor(x):
	sum=0
	i=0
	s=""
	bin=Stack()
	while x >= 1:
		bin_num=x%2
		x=int(x/2)
		bin.push(str(bin_num))
	while bin.isEmpty()==False:
		s=s+str(bin.peek())
		bin.pop()
	while i<len(s):
		if s[i]=="0":
			sum=sum+(2**(len(s)-i-1))
		i=i+1
	return sum
r=randint(1000,100000)
print r
for i in range(r):
	x=randint(1000,100000)
	print x
	k=Xor(x)
	num=input()
	if num!=k:
		print 'Wrong answer,no flag for you!'
		exit(0)
print 'Success, the flag is xiomara{link_lists_are_cool_btw}'

