#functions task day 11
'''Task 1: Add Function
Write a Python function named add that takes two arguments a and b and
returns their sum.
'''
def add(a,b):
    print(a+b)
add(2,7)
add(3,9)
'''Task 2: Square Function
Write a Python function named square that takes a number x as input and
returns its square.
'''
# method 1
def square(X):
    return X**2
obj=square(10)
print(obj)
# method2
result=lambda a:a**2
print(result(4))
import math
print(math.sqrt(100))
'''Task 3: Factorial Function
Write a Python function named factorial that takes a positive integer n as
input and returns its factorial.
'''
def function(n):
    import math
    print(math.factorial(n))
function(5)
'''Task 4: Maximum Function
Write a Python function named maximum that takes a list of numbers as input and
returns the maximum value in the list.'''
def Maximum(a):
    list=[2,4,6,7,9]
    import math
    print(max(list))
Maximum(list)
'''Task 5: Reverse Function
Write a Python function named reverse that takes a string s as input and
returns its reverse.
'''
def reverse(s):
   return s[::-1]
print(reverse("vivek"))
print(reverse("vani"))
'''Task 6: Check Prime Function
Write a Python function named is_prime that takes a positive integer n as input
and returns True if n is prime, otherwise False .
'''
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
prime=is_prime(4)
print(prime)
'''Task 7: Fibonacci Function
Write a Python function named fibonacci that takes a positive integer n as
input and returns the n th Fibonacci number.
'''
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end="")
        a,b=b,a+b
fibonacci(10)
'''Task 8: Palindrome Function
Write a Python function named is_palindrome that takes a string s as input and
returns True if s is a palindrome, otherwise False .
# '''
def is_palindrome(s):
    reverse=s[::-1]
    if s==reverse:
        print("True")
    else:
        print("False")
is_palindrome("vive")
'''Task 9: Sum of Squares Function
Write a Python function named sum_of_squares that takes a list of numbers as
input and returns the sum of the squares of those numbers.
'''
def sum_of_squares(n):
    list_2=0
    for i in n:
       list_2 += i**i
       return list_2
print(sum_of_squares([8,9,5,7]))
''' task 10  write a python function named average that takes a list of numbers as input and
returns the average value.'''
def average(n):
    length=len(n)
    average=(sum(n))/length
    print(average)
average([1,2,3,])



        

    

    
