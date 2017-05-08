#! /usr/bin/python

#	➭ The code calculates the starting point (variable limit in our code) corresponding to point x
#	➭ The value for the limit calculation is taken from 1 to n = (x+y)
#	➭ Then the difference between n and y is taken
#	➭ This difference is added to the limit. This is the final value!


def answer(x, y):

	#	1 is decremented as array starts from 0 in ours, but starts from 1 in Google challenge
	
	x = x-1
	y =y-1
	n =x+y 
	limit = 1
	for i in range(1,n+1):
		limit = limit + i
	print limit
	d = n -y
	limit1 = limit +d
	print limit1

answer(5,10)
