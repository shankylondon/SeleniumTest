
"""""
my_tup= ('shashank', 'ram')
my_tup= print(my_tup+('preeti', 'pratibha'))

print(my_tup)

my_list=['green', 'yellow','red']
my_list.append('pink')
my_list.extend(['a','b'])
my_list.insert(3,'joy')
print(my_list)

for my_list in my_list[1:3]:
    print('the current fruit is' +" " +my_list)

print('good bye')


weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)

for num in range(6):
    print(num*2)

    for num1 in range(5):

        print('attempt',num, num1*".")

"""
""""
count=0
for num in range(1,10):
    if (num%2==0):

        count=count+1
        print(num)

print('we have the total count as ',count)
"""


f = open('my data','r')
print(f.read())










