# -*- coding:utf-8 -*-
import json

strJson = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

obj = json.loads(strJson)

print obj
print obj.get('a')
print strJson