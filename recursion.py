num=input('Please input a number: ')
num=int(num)
def factorialUsingRecursion(n): 
    if (n == 0): 
        return 1; 
  
    # recursion call 
    return n * factorialUsingRecursion(n - 1)





#print(factorialUsingRecursion(num))

print(num,factorialUsingRecursion(num))
