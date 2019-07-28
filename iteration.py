def factorialUsingIteration(n):
	res=1;

#using iteration
	for i in range(2,n+1):
		res*=i;
	return res;
num=input("Please input a number: ")
num=int(num)

print(num,factorialUsingIteration(num))



