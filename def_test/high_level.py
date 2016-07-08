# --*-- coding:utf-8 --*--
def slices(listName):
    newList = listName[2:3]
    for value in newList:
        print value
# slices(['哈士奇','泰迪','藏獒','茶杯犬'])

def iterationName():
    list1 = [1,2,3]
    for value in list1:
        print value
    dit1 = {'name':'wangxiaoming','age':18,'city':'Beijing'}
    for key in dit1:
        print key
    for value in dit1.itervalues():
        print value
    for k,v in dit1.iteritems():
        print 'key is {0}, value is {1}'.format(k,v)
iterationName()
