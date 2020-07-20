
"""""
print('enter the value range\n')
marks=int(input())
for num in range(marks):
    if(num%3==0 and num%5==0):
        print('fizzbuzz')
    elif(num%3==0):
        print('fizz')
    elif(num%5==0):
        print('buzz')
    else:
        print(num)
"""
"""""
n=int(input())
sum=sum(range(1,n))
print(sum)

"""
"""""
#adding the numbers in list

n=int(input("enter the number of elements to be inserted"))
a=[]
for i in range(n):
    elem=int(input("enter the element"))
    a.append(elem)
avg=sum(a)/n

"""
"""""
#Reversing the number

num=int(input("Please enter the number"))
Rev=0
while(num>0):
    dig=num%10
    Rev=Rev*10+dig
    num=num//10
print(Rev)

"""""
"""""
#Total sum of digits in a number

num=int(input("Please enter the number"))
Sum=0
while(num>0):
    dig=num%10
    Sum=Sum+dig
    num=num//10
print(Sum)

"""""
"""""
#To check if palindrome.

num=int(input("Please enter the number: "))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10

if(rev==temp):
    print("the number is palindrome")
else:
    print("its not a palindrome")
    
"""""

#To print the table of number

num=int(input('please enter the number'))

for i in range(1,11):
    table=num*i
    print( num ,'x', i ,'=',table)









