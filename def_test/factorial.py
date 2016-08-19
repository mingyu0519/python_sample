# coding=utf-8

def run(n):
	if n==1:
		return 1
	else :
		return n * run(n-1)

def run1(n):
	result = 1
	for x in xrange(1,n+1):
		result = result * x
	return result

if __name__ == '__main__':
	result = run(20)
	print result

	res = run1(20)
	print res
