import random
programm = int(input("Enter 1 or 2 or 3 or 4 or 5 or 6 or 7: "))
match programm:
    case 1:
        sum = 0
        for i in range(1, 11):
            sum += i

        print(f"sum 1 to 10: {sum}")
