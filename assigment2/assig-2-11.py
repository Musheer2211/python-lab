sent = input('Enter a sentence : ')

words = sent.split()


digits = 0
lower = 0
upper = 0


for word in words:
    for i in word:
        if i >= '0' and i <= '9':
            digits += 1
        elif i >= 'a' and i <= 'z':
            lower += 1
        elif i >= 'A' and i <='Z':
            upper += 1

print(f'This sentence has {len(words)} words')
print(f'This sentence has {digits} digits')
print(f'{upper} upper case letters')
print(f'{lower} lower case letters')


