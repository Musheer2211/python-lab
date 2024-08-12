string = list(input("Enter a String : "))

string[0],string[-1] = string[-1],string[0]

string = str().join(map(str,string))

print(string)