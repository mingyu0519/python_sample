# coding=utf-8

def run():
    i = 101
    while i < 1000:
        b1 = i/100
        b2 = i%100/10
        b3 = i%100%10
        if (b1*b1*b1 + b2*b2*b2 + b3*b3*b3) == i:
            print "{0}是一个水仙花数".format(i)
        i = i + 1

if __name__ == '__main__':
    run()
