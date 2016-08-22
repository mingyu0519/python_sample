# -*- coding:utf-8 -*-

# 使用for循环递减得出每一位的字母
def reverse(str):
	r = ''
	for x in xrange(len(str)-1, -1 , -1):
		r = r + str[x]
	return r

# 先转换成list，再反转list，再使用join方法转换list为字符串
def reverse2(str):
	li = list(str)
	li.reverse()
	str = "".join(li)
	return str

# 以反向截取整个字符串
def reverse3(str):
	return str[::-1]

# str默认转换为list类型，然后翻转，再转化为字符串
def reverse4(str):
	return "".join(reversed(str))

initStr = 'abcdefghigklmnopqrstuvwxyz'

print initStr

print reverse(initStr)

print reverse2(initStr)

print reverse3(initStr)

print reverse4(initStr)