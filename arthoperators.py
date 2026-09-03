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

print("passed:",marks >= 40)]