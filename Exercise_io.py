import os

#Task1: Accept two numbers from the user and calculate multiplication

a,b,c=input('enter the numbers you want to multiply:').split()
print(a,b,c)

b=int(input('enter the numbers you want to multiply:'))
print(f'multiplication of {a} and {b} is {a*b}')


#Task2:Display “My Name Is James” as “My**Name**Is**James”
print('My', 'Name', 'Is', 'Rajesh',sep='&&')


#task3:
a=int(input('enter the decimal number:'))
print(f'octa num of {a} is {oct(a)}')
print('%o,'%(8))
a=458.42305
print('%.2f' % a)

#a,b,c,d,e=float(input('enter the numbers you want to multiply:'))

floatNumbers = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)

print("User List is ", floatNumbers)


count = 0
with open("/Users/rgangabattina/Desktop/Personal/work_study/Study/Python/personal-git/test.txt", "r") as fp:
    lines = fp.readlines()
    lenth = len(lines)
    count = 1
with open("/Users/rgangabattina/Desktop/Personal/work_study/Study/Python/personal-git/newtest.txt", "w") as fp:
    for line in lines:
        if (count%5==0):
            count += 1
            continue
        else:
            fp.write(line)
        count+=1

#Task8 :display above data using string.format() method
totalMoney = 1000
quantity = 3
price = 450
print('I have {} dollars so I can buy {} footballs for {} dollars'.format(totalMoney,quantity,price))


#Question 9: How to check file is empty or not

print(os.stat("/Users/rgangabattina/Desktop/Personal/work_study/Study/Python/personal-git/test.txt").st_size)

#Question 10: Read line number 4 from the following file
with open("/Users/rgangabattina/Desktop/Personal/work_study/Study/Python/personal-git/test.txt", "r") as fp:
    lines=fp.readlines()
    print(lines[2])