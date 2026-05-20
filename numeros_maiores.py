print("Ola irei dizer qual numero é maior entre 3 outros numeros")

n1 = float(input("informe o primeiro valor: "))
n2 = float(input("informe o segundo valor: "))
n3 = float(input("informe o terceiro valor: "))

if (n1 > n2) and (n1 > n3):
    print(f"O maior valor é {n1}")
elif (n2 > n1) and (n2 > n3):
    print(f"O maior valor é {n2}")
else:
    print (f"O maior valor é {n3}")
    

