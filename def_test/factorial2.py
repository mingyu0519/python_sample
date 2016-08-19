# coding=utf-8

def test(n):
	if n==1:
		return 1
	else:
		return n * test(n-1)

if __name__ == '__main__':
	result = test(5)
	print result