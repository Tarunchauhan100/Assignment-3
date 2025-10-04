#   Task 1 Calculate Factorial Using a Function
# creating a function 
def factorial (x):
    if x == 1 :
        return 1 
    else:
        #calling a function
        return(x*factorial(x-1))
num = int(input("Enter a Number :"))
print("The factorial of",num,"is :",factorial(num))
