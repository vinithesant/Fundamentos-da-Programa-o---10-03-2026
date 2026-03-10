# Programa de Calculadora 10 03 2026
# Vinicius Sant

print(" > CALCULADORA VINI-BOX 1.0 < ")
print("                              ")

op = input ("Digite 1-SOMAR, 2-DIVIDIR, 3-DIVIDIR, 4-MULTIPLICAR, 5-POTENCIA, 6-RADICIAÇÃO")
op = int(op)

a = input("Entre com o 1º número")
a = int(a)

b = input("Entre com o 2º número")
b = int(b)

if (op == 1):
	print(a + b)
    
elif (op == 2):
    print(a - b)
    
elif (op == 3):
    print(a / b)
    
elif (op == 4):
    print(a * b)
    
elif (op == 5):
    print(a ** b)
    
elif (op == 6):
    print(a ** (1/2))

else: 
     print("")
     
print("                  ")
print("Obrigado pela aula")
print("~Vini")
input ()