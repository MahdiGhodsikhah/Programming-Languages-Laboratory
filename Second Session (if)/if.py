programm = int(input("Enter 1 or 2 or 3 or 4 or 5 or 6 or 7: "))
match programm:
    case 1:
        score = float(input("Enter your Score number: "))
        if (score <= 20):
            if (score >= 17):
                print(f"A - your score {score}- your great.")
            elif (score >= 15):
                print(f"B - your score {score}- your good.")
            elif (score >= 10):
                print(f"C - your score {score}- not bad.")
            else:
                print(f"your score {score}- kharab kardi pesar jan.")
        else:
            print("the entry is out of range")
    case 2:
        age = int(input("Enter your age: "))
        li = input("do you have lisence (y/n): ") == 'y'
        isdrunk = input("Are you drunk (y/n): ") == 'y'
        
        if (age >= 18 and li and not isdrunk):
            print("you can drive 😁")
        else:
            print("you can't drive 😅")
    case 3:
        amount = float(input("How much did you buy ? "))
        tier = input("enter your tier (gold / silver / bronze)").lower()
        
        if (amount < 10_000_000):
            if (tier == 'gold'):
                amount *= 0.85
                print(f"you have 15% off and you should pay {amount}")
            elif (tier == 'silver'):
                amount *= 0.90
                print(f"you have 10% off and you should pay {amount}")
            elif (tier == 'bronze'):
                amount *= 0.95
                print(f"you have 5% off and you should pay {amount}")
        else:
            if (tier == 'gold'):
                amount *= 0.80
                print(f"you have 20% off and you should pay {amount}")
            elif (tier == 'silver'):
                amount *= 0.85
                print(f"you have 15% off and you should pay {amount}")
            elif (tier == 'bronze'):
                amount *= 0.90
                print(f"you have 10% off and you should pay {amount}")
    case 4:
        number = int(input("Enter a number: "))
        if number == 0:
            print("Your number is Zero")
        elif number > 0:
            print(f"{number} is Positive")
            if number % 2 == 0 :
                print(f"{number} is Even")
            else:
                print(f"{number} is Odd")
        else:
            print(f"{number} is Negative")
            if number % 2 == 0:
                print(f"{number} is Even")
            else:
                print(f"{number} is Odd")
