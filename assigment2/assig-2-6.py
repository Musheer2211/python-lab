cel_or_fre = input("Celsius or Fahrenheit (C/F) : ")

if cel_or_fre == 'C' or cel_or_fre == 'c':
    cel_or_fre = 'Celsius'
elif cel_or_fre.lower() == 'f':
    cel_or_fre = 'Fahrenheit'
else:
    raise Exception('Input valid option')

num = int(input(f'Enter Temperature in {cel_or_fre} : '))

if cel_or_fre == 'Celsius':
    print(f'Temperature in Fahrenheit is {(num*1.8) + 32}')
else:
    print(f'Temperature in Celsius is {(num/1.8) - 32}')
