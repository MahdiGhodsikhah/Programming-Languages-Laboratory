programm = int(input("Enter 1 for first programm (card) and Enter 2 for second programm (your salary): "))


if (programm == 1):
    print("-----------first programm running1-----------")
    name = input("Enter Your name: ")
    year_of_birth = int(input("Enter Your Year of birth: "))
    height = int(input("Enter Your Height: "))
    age = 1405 - year_of_birth

    print("---------------------------------------------")
    print(f"\tWellcome {name}")
    print(f"\tYour Year of birth is : {year_of_birth}")
    print(f"\tYour age is {age}")
    print(f"\tYour Height is : {height}")
    print("---------------------------------------------")