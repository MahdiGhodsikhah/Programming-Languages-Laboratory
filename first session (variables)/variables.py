programm = int(input("Enter 1 for first programm (card) and Enter 2 for second programm (your salary): "))


if (programm == 1):
    print("-----------first programm running1-----------")
    name = input("Enter Your name: ")
    year_of_birth = int(input("Enter Your Year of birth: "))
    height = float(input("Enter Your Height: "))
    age = 1405 - year_of_birth

    print("---------------------------------------------")
    print(f"|\tWellcome {name}")
    print(f"|\tYour Year of birth is : {year_of_birth}")
    print(f"|\tYour age is {age}")
    print(f"|\tYour Height is : {height}")
    print("---------------------------------------------")
else:
    print("-----------second programm running-----------")
    salary = float(input("Enter Your Salary: "))
    
    insurance = salary * 0.07
    salary_after_insurance = salary - insurance
    
    tax = salary_after_insurance * 0.09
    final_salary = salary_after_insurance - tax
    
    print("---------------------------------------------")
    print(f"|\tInitial Salary: {salary}")
    print(f"|\tInsurance (7%): {insurance}")
    print(f"|\tSalary After Insurance: {salary_after_insurance}")
    print(f"|\tTax (9%): {tax}")
    print(f"|\tFinal Salary: {final_salary}")
    print("---------------------------------------------")