soma= 0
while True:
    num = int(input("Digite um número qualquer, ou     zero para sair:"))

    if num == 0:
        break
    soma +=num
print(f"Total da soma dos números: {soma}")