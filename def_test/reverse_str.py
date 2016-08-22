# -*- coding:utf-8 -*-

def reverse(str):
	r = ''
	for x in xrange(len(str)-1, -1 , -1):
		r = r + str[x]
	return r

def reverse2(str):
	li = list(str)
	li.reverse()
	str = "".join(li)
	return str

def reverse3(str):
	return str[::-1]

initStr = 'abcdefghigklmnopqrstuvwxyz'

print initStr

print reverse(initStr)

print reverse2(initStr)

print reverse3(initStr)