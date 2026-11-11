programm = int(input("Enter 1 for first programm (Score) or Enter 2 for second programm (Drive): "))
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
