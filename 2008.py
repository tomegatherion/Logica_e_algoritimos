#Operações simples de multiplicação
Fristnumeber = 2
Secondnumber = 3

product = Fristnumeber * Secondnumber
print(product)



#Operações simples de multiplicação com numeros inteiros
Fristnumeber = int(input("Fristnumber : "))
Secondnumber = int(input("Secondnumber : "))

product = Fristnumeber * Secondnumber
print(product)



#Operações simples de multiplicação com numeros reais
Fristnumeber = float(input("Fristnumber : "))
Secondnumber = float(input("Secondnumber : "))

product = Fristnumeber * Secondnumber
print(product)



#Operações de divisão inteira com numeros inteiros
Fristnumeber = int(input("Fristnumber : "))
Secondnumber = int(input("Secondnumber : "))

product = Fristnumeber // Secondnumber
print(product)



Fristnumeber = int(input("Fristnumber : "))
Secondnumber = int(input("Secondnumber : "))

product = Fristnumeber % Secondnumber
print(product)



#Operação de exponenciação
Fristnumeber = int(input("Fristnumber : "))
Secondnumber = int(input("Secondnumber : "))

product = Fristnumeber ** Secondnumber
print(product)



#Raiz quadrada
import math
math.sqrt(16)

#tabuada
print("Tabuada")
Fristnumber = int(input("Digite o Numero: "))
product0 = Fristnumber * 0
product1 = Fristnumber * 1
product2 = Fristnumber * 2
product3 = Fristnumber * 3
product4 = Fristnumber * 4
product5 = Fristnumber * 5
product6 = Fristnumber * 6
product7 = Fristnumber * 7
product8 = Fristnumber * 8
product9 = Fristnumber * 9
product10 = Fristnumber * 10

print(f"0  X {Fristnumber} = {product0}")
print(f"1  X {Fristnumber} = {product1}")
print(f"2  X {Fristnumber} = {product2}")
print(f"3  X {Fristnumber} = {product3}")
print(f"4  X {Fristnumber} = {product4}")
print(f"5  X {Fristnumber} = {product5}")
print(f"6  X {Fristnumber} = {product6}")
print(f"7  X {Fristnumber} = {product7}")
print(f"8  X {Fristnumber} = {product8}")
print(f"9  X {Fristnumber} = {product9}")
print(f"10 X {Fristnumber} = {product10}")


#Estrutura de repetição
for n in range (0,5):
    print(n)




#Estrutura de repetição
n = 0
while n < 5:
  print(n)
  n += 1



#lista
lista = [1,2,3,4,10]
for numero in lista:
    print(numero ** 2)


#tabuada com repetição
print("Tabuada")
Fristnumber = int(input("Digite o Numero: "))
n = 0
while n <11:
  product = Fristnumber * n
  print(f"{n} X {Fristnumber} = {product}")
  n += 1



#
palavra = "casa"
for letra in palavra:
    print(letra)



#  lista
gatinhos = {"Portugues": "gato",  "Ingles": "cat", "Francês": "chat", "Finlandês": "kissa"}
for chave, valor in gatinhos.items():
    print(chave, "->", valor)


























