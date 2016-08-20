# coding=utf-8

def run(n):
	i = 1
	for x in xrange(2,n+1):
		i = (i+1)*2
	return i

if __name__ == '__main__':
	result = run(10)
	print '猴子第一天一共摘了{0}个桃子'.format(result)