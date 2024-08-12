str1,str2 = map(list,input("Enter 2 strings :").split())

str1[0:2],str2[0:2] = str2[0:2],str1[0:2]
str1 = str().join(map(str,str1))
str2 = str().join(map(str,str2))
print(str1,str2)
