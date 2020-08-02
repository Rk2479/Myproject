from functools import reduce

def febc(num):
    fs=[0,1]
    for i in range(num):
        fs.append(reduce(lambda x,y:y+x,fs[-2:]))
    print(fs)

febc(5)


#Type 2 ###   My Idea #######

a=[0,1]
def febo(num):
    x=0
    y=1
    for i in range(num):
        y=y+x
        x=a[-1]
        a.append(y)
    print(a)

febo(10)
