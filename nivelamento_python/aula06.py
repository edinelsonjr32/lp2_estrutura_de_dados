#Estruturas de Repetição:
#variável = nome + sinal de atribuição e um valor 

x = 10
#print(x)

#reatribuição = alterar o valor de uma variável já existente
x = 12

#atualização de variável
x = x + 1

x = x - 1

#Atualização variável para realizar incremento e decremento de um valor de um contador


#Estrutura de repetição While:
"""
CHECKLIST CRIAÇÃO DE UMA ESTRUTURA DE REPETIÇÃO WHILE
1 - Uso de uma palavra reservada while
2 - Critério de parada -> expressão boolena 
3 - Delimitação do nosso bloco de execução por meio do simbolo ":"
4 - Instruções individuais
5 - Manipulação do Contador(incremento ou decremento)
"""
"""
contador = 0 # valor da quantidade de interações que eu quero executar

while contador <= 20:
    print(contador)
    contador = contador + 1
print('.')
print("Fim da execução") 
"""
#Uso do comando break
"""
while True:
    texto = input('Insira um texto que você deseja imprimir na tela (caso queira finalizar o programa, digite /sair) ')
    if texto == '/sair':
        print('Você saiu do Programa! ')
        break
    else:
        print(texto)
"""

"""
Estrutura de repetição For
--checklist--
1 - a palavra reservada for
2 - nosso valor que vamos usar como contador
3 - simbolo de criação de um bloco de instruções ':'
4 - instruções
"""
"""
for x in range(10):
    print(x)
print('Fim da Execução! ')
"""
"""
valor = input("Insira a quantidade de números a ser inserida na lista (lista inicia com 0): ")
valor = int(valor)# caso o valor repassado seja de outro tipo. 

lista = []

for x in range(valor):
    lista += [x*3]
print(lista)
"""

contador = 0

while contador < 20:
    print(contador)
    contador = contador + 1
print('.')
print("Fim da execução") 








