from unittest import case

num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

op = (input("Digite uma opcao:(+,-,*,/)"))

match op:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)

    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Acabou")