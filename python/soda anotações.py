# int: numero inteiro {18, 7, 69}
# str: palavras {cristiano, ronaldo, sexo}
# float: numero quebrado {3.14, 15.9, 666.69}
# boll: binary {true, false}
# list [] / array: listar

idade = 15
nome = 'henrique'
altura = 1.73
valor = True
lista = [idade, nome, altura, valor]

print (lista[2])
print (idade, type(idade))
print (nome, type(nome))
print (altura, type(altura))
print (valor, type(valor))
print (lista, type(lista))

# > maior
# < menor
# >= maior ou igual
# <= menor ou igual
# != diferente
# == igual

# and: e
# or: ou

# + adição
# - subtração
# * multiplicação
# / divisão
# % sobra da divisão
#

#variavel. : armazenar informação
#isspace() só espaço
#isnumeric() só numero
#str[] caracter especifico
#capitalize() primeira maiuscula
#upper() tudo maiusculo
#lower() tudo minusculo

#count ('texto') conta quantas vezes aparece na str
#startswith ('X') verifica se começa com X
#endswhith ('X') verifica se termina com X
#len(x) conta quantos caracteres tem na str
#max vê qual é o maior numero
#min vê qual é o menor numero

#dicionario {} 



space = "\n ////////////////////////////////////////////////// \n"
print(space)

dicionario = {
  'Nome' : 'Henrique',
  'Idade' : 15,
  'Cidade': 'Pompeia'
}

dicionario['Saldo Bancario'] = '0,00'

print (dicionario)
#append / insert: adicionar novo item a lista
#remove: apagar item da lista

# """ permite abrir uma str mais longa

saldobancario = 'RS:00,00'
print(idade in lista)
lista.remove(idade)
lista.insert(0, saldobancario)
print(lista)
suicidio = 'legal'
print(suicidio.count('l'))

contador = 0

#while: enquanto

#break: quebra o loop
#continue: passa a linha
#pass: SLA VIADOKKKKKKKKK (pode ser usado no else)

print('\n aaa')
while contador < len(lista):
  contador += 1
  if contador == 1:
    continue
  if contador > 3:
    break
  print(lista[contador], contador, '\n')

#def: definir uma função
#def (): 

print(space)

def canetaazul(num1, num2):
  print(num1 + num2)
  print('Caneta Azul')
  print('Azul Caneta')
  canetavermelha()

def canetavermelha():
  print('canetavermelhaaaaaaa')
  
canetaazul(40, 70)

def listadoinferno(lista):
  contador = 0
  while contador <= len(lista) -1:
    print(lista[contador])
    contador += 1

listadoinferno(['eu', 'demonio', 'belzebub', 'bolso'])

def somafoda(num3, num4):
  return print('agua')
  return num3 + num4

resultado = somafoda(70, 67)

print(resultado)

print('vagabunda')

print(space)

# for: pro português "para", é basicamente um "while" bom para loop

listafor = ['a', 'b', 'c', 'd']

for item1 in listafor:
  print(item1)

for i in range(5):
  print(i)

lista10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(space)

for item2 in lista10:
  if item2 % 2 == 0:
    print(item2, 'é par')
  else:
    print(item2, 'é impar')

# X[: -1] = é usado para remover um caracter
# X[::-1] = é usado para ler a palavra de tras para frente

guilherme = 'guilherme'

print(guilherme[:-2])


