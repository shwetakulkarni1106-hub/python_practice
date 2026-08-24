num1=int(input("enter number1: "))
num2=int(input("enter number1: "))

operation=input(("enter which operation you want to perform(+,-,*,/) : "))

match operation:
    case "+":
        print("num1+num2:",num1+num2)
    case "-":
        print("num1-num2: ",num1-num2)   
    case "*":
        print("num1*num2: ",num1*num2)   
    case "/":
        print("num1/num2: ",num1/num2)   
             
              