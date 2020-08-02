from functools import reduce

def febc(num):
    fs=[0,1]
    for i in range(num):
        fs.append(reduce(lambda x,y:y+x,fs[-2:]))
    return fs

result=febc(5)
print(result)