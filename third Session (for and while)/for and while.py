import random
programm = int(input("Enter 1 or 2 or 3 or 4 or 5 or 6 or 7: "))
match programm:
    # sum 1 to 10
    case 1:
        sum = 0
        for i in range(1, 11):
            sum += i

        print(f"sum 1 to 10: {sum}")
    # password checker
    case 2:
        password = "1234"
        attempts = 3
        while attempts > 0:
            entry_pass = input(f"enter a password (attempts{attempts}):")
            if password == entry_pass:
                print("access verified, wellcome")
                break
            else:
                attempts -=1
                print("wrong password")
    # game and pass generator
    case 3:
        while True:
            print("1. pass generator")
            print("2. guess number")
            print("3. exit")

            choice = int(input("choose option (1-3):"))
            # password
            if choice == 1:
                chars = ['!', '@', '#', '$', '%', '&', '^', '*', '(', ')', '-']
                length = int(input("enter password lenght: "))
                password_generated = ''.join(random.choice(chars) for _ in range(length))
                print(password_generated)
            # random number
            elif choice == 2:
                random_number = random.randint(1, 100)
                attempts = 7
                for i in range (7):
                    guees_number = int(input(f"enter a number between 1 and 100 (attempts {attempts}) :"))
                    attempts -= 1
                    if guees_number == random_number:
                        print("you win")
                        break
                    elif guees_number < random_number:
                        print("number is bigger.")
                    else:
                        print("number is smaller.")
                else:
                    print("you lost.")
                    print(f"the number is :{random_number}")

            elif choice == 3:
                break
            else:
                print("invalid")
    #Factorial
    case 4:
        number = int(input("enter a number: "))
        factorial = 1
        if number > 0:
            for i in range(1, number + 1):
                factorial *= i
            print(f"factorial {number} is: {factorial}")
        else:
            print("please enter a positive number!")
    case 5:
        for i in range(1, 51):
            if i == 42:
                break
            if i % 5 == 0:
                continue
            if i % 3 == 0:
                print(i)
    case 6:
        
