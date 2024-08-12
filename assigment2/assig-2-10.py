num = input('Enter a number : ')

if num == num[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')

count = {x:num.count(x) for x in num }

for i in count:
    print(f'{i} appears {count[i]} times')


