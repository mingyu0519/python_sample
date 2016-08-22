# -*- coding:utf-8 -*-
import json

obj = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
encodejson = json.dumps(obj)

print repr(obj)
print encodejson