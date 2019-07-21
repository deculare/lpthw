import csv
exampleFile = open('db.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
i=0
for i in range (0,26):
	i=i+1
	a= exampleData[i][0]
	b= exampleData[i][1]
	c= a+b
	print(f"My name is {a} and my age is {b}.")
	print (c)
