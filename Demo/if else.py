
"""""

marks=int(input())
if (marks>80):
    print('Grade A')
elif (marks>60) and (marks<=80):
    print('Grade B')
elif (marks<=59) and (marks>40):
    print('Grade c')
else:
    print('Grade D')
    
"""""

num=int(input('print the number'))

if (num<0):
    print('enter a valid value')
else:
    sum=0
    while(num>0):
        sum=sum+num
        num=num-1
print(sum)





