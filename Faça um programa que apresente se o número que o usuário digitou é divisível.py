n = int(input("Digite um número: "))

if n % 3 == 0 and n % 5 == 0:
    print(f"{n} é divisível por 3 e por 5.")
else:
    print(f"{n} não é divisível por 3 e por 5.")
