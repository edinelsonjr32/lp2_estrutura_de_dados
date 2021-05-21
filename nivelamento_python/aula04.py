import math


#Trabalharmos com as funções de conversão de tipo.
"""
numero = "75"


print(type(numero))

print(numero)

resultado = int(numero)

print(resultado)

print(type(resultado))




numero_extenso = "dois"

print(int(numero_extenso))

"""


"""
função de conversão para float

numero_em_string = float("40.5")

print(type(numero_em_string))

inteiro = 40

print(inteiro)

numero_em_inteiro = float(40)

print(numero_em_inteiro)
print(type(numero_em_inteiro))

"""

#Convertendo para string

"""
numero_inteiro_em_string = str(40)

print(numero_inteiro_em_string)

print(type(numero_inteiro_em_string))

valor_booleano_para_string = str(True)

print(valor_booleano_para_string)

print(type(valor_booleano_para_string))

print("O resultado é: " + valor_booleano_para_string)

"""
#Funções matemáticas:

#print(math)

cosseno = math.cos(20)

#print(cosseno)

tangente = math.tan(20)

#print(tangente)

seno = math.sin(20)
#print(seno)

#calcular a raiz quadrada

"""
raiz_quadrada = math.sqrt(64)

print(raiz_quadrada)

print(type(raiz_quadrada))

"""
#processo de criação de uma função

"""
Sintaxe de uma função sem argumentos.

def nome_funcao():
   instrucao1
   instrucao2
      instrucao2.1
      instrucao2.2
   instrucao3
instrucao4


Defnição de instrução com argumento.

def nome_funcao_dois(argumento1):
   instrucao1
      instrucao1.1
         instrucao1.1.1
    print(argumento1)
instrucao2
"""

def imprime_meu_nome():
   print("Imprimindo o nome Edinelson Junior, na função imprime_meu_nome")

#print("Não está na função")

#imprime_meu_nome()


"""
print(type(imprime_meu_nome))

nome = imprime_meu_nome()

print(nome)


"""

def nome():
   return "Edinelson"


#ele começa de 0 e executa n vezes aquele bloco de intruções
def repetir_nome(quantidade_repeticoes):
   for i in range(0, quantidade_repeticoes):
      print(nome())
      i = i+1
      

#print(nome())

print(repetir_nome(10))



