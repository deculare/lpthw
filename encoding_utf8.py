#unicode straing
string ='python!'

#print string
print("The string is:", string)

#default encoding to utf-8
string_utf=string.encode('UTF-8','strict')

#print result
print('Ther encode version is :', string_utf)
