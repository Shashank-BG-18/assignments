#Code to calculate Payabale Salary

#Taking input from user
emp_id=int(input("Enter the employee id : "))
name=input("Enter your name : ")
job=input("Enter your job : ")
basic_pay=float(input("Enter your basic pay : "))

#Setting the allowance and calculating payable_salary
allowance = 0.05*basic_pay if job=="manager" else 0.08*basic_pay if job=="developer" else 0.1*basic_pay if job=="analyst" else 0
payable_salary=basic_pay+allowance

#Printing the output
print(f"Employee {name}, with id {emp_id}, has an allowance of {allowance}, and has a payable salary of {payable_salary}")
