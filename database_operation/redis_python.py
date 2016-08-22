# coding=utf-8
import redis

r = redis.Redis(host='localhost',port=6379,db=0)

# 设置键值对
r.set('book', '鱼羊野史')

# 获取key的value
result = r.get('book')
print result

# 获取所有的key
keys = r.keys()
print keys

# 获取当前数据库的数据条数
number = r.dbsize()
print number
