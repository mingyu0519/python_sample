# coding=utf-8

def test():
	n = 0
	for x in xrange(101,200):
		for y in xrange(2,x):
			if x%y == 0:
				n = n + 1
				break
		if n == 0:
			print "{0}是一个素数".format(x)
		n = 0

if __name__ == '__main__':
	test()