# coding=utf-8

def run(n):
	k = 2
	while k <= n:
		if k == n:
			print n
			break
		elif n%k == 0:
			print '{0} *'.format(k),
			n = n/k
		else:
			k = k + 1

if __name__ == '__main__':
	run(12)