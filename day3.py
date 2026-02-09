#data structures and data types
student_details=[23,8.9,"vivek",[1,4.7,"mango",(7,0)],(2,3.6,[8,9.0],[9,0,6.9,"rahul"])]
print(student_details)
#defining a set
employees_id={119,78,90,67,89,45,78,56,36,78,98,67,78}
print(employees_id)
#string concatination
first_name="rahul"
last_name="gangadhari"
result=first_name+" "+last_name
print(result)
#repeating string
student_name="pratap reddy \n"
result=student_name*3
print(result)
# using python key word
else=789
if=34
result=if+else
print(result)
# when we are using the else or if statements it is showing invalid syntax and program is not executing
# type conversion from float to int
person_age=7.0
converting_type=int(person_age)
print(converting_type)
# type conversion from integer to string
person_age=700
converting_type=str(person_age)
print(converting_type)
print(type(converting_type))
# simple input & output
user_age=int(input("enter the user age:"))
print("our sarpanch age is",user_age)
# exercise:
# printing patterns using print statements:
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
# dictionary use
library_book={"title":"java programming","author":"james gosling","publication year":"1995",}
mobile_details={"manufacturing_year":2020,"brand":"oppo","place":"hyderabad"}
print(library_book,mobile_details)
# string operatons
number_1=float(input("enter the number1:"))
print(number_1)
# concatinate strings
start_name=input("enter the start_name:")
last_name=input("enter the last_name:")
result=start_name+" "+last_name
print(result)
#create a prg that takes user input for their age,converts it to an integer adds 5,and then prints result
user_age=input("enter the age:")
convert_toint=int(user_age)
#print(convert_toint)
print(type(convert_toint))
convert_toint +=5
print(convert_toint)
# building acalculator program take sthe input from the user 
input_1=float(input("enetr the number1:"))
input_2=float(input("enter the number2:"))
print(f" addition:{input_1+input_2}\n subtraction:{input_1-input_2}\n multiplication:{input_1*input_2}\n division :{input_1/input_2}\n modulous:{input_1%input_2}\n floor division :{input_1//input_2}\n exponmential {input_1**input_2}")

######################jan 5/01/2026################
#list
sample_data=[78,9.0,"kprit"]
print(type(sample_data))
print(sample_data)
sample_data.append("ramu")
print(sample_data)




