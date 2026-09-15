
#arthimetic operator

a = 10
b = 3

print("Addition:", a + b)
print("subtraction:",a - b)
print("multiplication:",a * b) 
print("division:",a / b)
print("floor division:",a // b)
print("remainder:",a % b)
print("power:",a ** b)

#simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("subtraction:",a - b)
print("multiplication:",a * b)
print("division:",a / b)
print("floor division:",a // b)
print("remainder:",a % b)
print("power:",a ** b)


  #student marks calculator
a = input("Enter student name: ")
b = int(input("Enter student marks: "))

subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))
subject4 = int(input("Enter marks for subject 4: "))
subject5 = int(input("Enter marks for subject 5: "))
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
average_marks = total_marks / 5
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

#shopping bill calculator
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
total_price = item1 + item2 + item3
print("Total Price:", total_price)

#assignment operator
x = 10

x +=5
print(x)

x -= 2
print(x)

x *= 3
print(x)


#bank balance 
balance = 10000
  
deposit = 5000
balance += deposit 

print("After Deposit:", balance)

withdrawal = 2000
balance -= withdrawal

print("After Withdrawal:", balance)

 #age eligibility checker 
age = int(input("Enter your age: "))

print("eligible:",age >= 18)

#pass or fail checker
marks = int(input("enter mark:"))

print("passed:",marks >= 40)

#logical operators
age = 25
citizen = True

print(age)

#atm eligibility  checker
balance = 10000
withdraw = 5000

print()

#identity operators
a = 10

print(a is None)
print(a is not None)

#bitwise operators
a = 5
b = 3

print(a & b)  
print(a | b) 
print(a ^ b)  

#electric city bill calculator
units = float(input("Enter number of units consumed: "))

rate = 6

bill_amount = units * rate
print("Total Bill Amount:", bill_amount)

#triangle expense calculator
travel= float(input(" travel expense: "))
food= float(input(" food expense: "))
hotel= float(input(" hotel expense: "))

total_expense = travel + food + hotel
print("Total Expense:", total_expense)

#accessing elements of a list
marks = [80, 90, 75 ,85]
print(marks[0])
print(marks[1])
print(marks[2])

#changing elements of a list
marks = [80, 90, 75]

marks[1] = 95
print(marks)

marks = [75 ,95,86,70,69,98]

marks[1] = 100
marks[3] = 80
marks[5] = 90
print(marks)

#remove elements from a list
marks = [80, 90, 75]

marks.remove(90)

print(marks)

#tuples in python
#tuple is a collection of multiple values that is ordered and cannot be changed after creation
student = ("mounish", 98, "python")

print(student[0])

#immutable nature of tuples
student = ("mounish", 98, 85.5)

student[1] = 22
#this gives an error because we  cannot modify a tuple

#tuples are immutable, meaning their elements cannot be changed after creation. they are defined using parentheses () and can contain elements of different data types.
numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))  

numbers = (10, 20, 30, 40,)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable. it is defined using curly braces {} or the set() constructor.
numbers = {10, 20, 30, 20, 10}

print(numbers)

#add values to a set
subjects = {"python", "java"}

subjects.add("SQL")

print(subjects)

#remove values from a set
subjects.remove("java")

print(subjects)

#sets do not allow duplicate values
numbers = {1, 2,2,3,3,4,}

print(numbers)

#dictionaries in python 
#dictionary is a collection of key-value pairs that is unord
student = {
    "name" : "mounish",
    "age"  : 00,
   "course":"python"
}
 #access element in dictionary
print(student["name"])
print(student["age"])
print(student["course"])

#add new data to a dictionary
student["city"] = "vijayawada"

print(student)

 #popitem() removes the last inserted key-value pair 
student = {
    "name" : "mounish",
    "age"  : 00,
   "course":"python"
     }

student.popitem()
print(student)

student = {
    "name" : "mounish",
     }

student.setdefault("age", 18)

print(student)

















