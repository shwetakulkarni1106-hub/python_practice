a=int(input("enter value of a inbetween(1 to 10): "))

match a:
    case 1:
        print("you won car")
    case 3:
        print("you won bike")
    case 5:
        print("you won mobile")
    case _:
        print("best luck next time")            