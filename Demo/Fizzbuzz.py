
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
n=int(input())
sum=sum(range(1,n))
print(sum)
