#Estruturas condicionais -> Vou executar ações dependendo da condição
#Booleano -> True ou False
#Expressão Booleana -> Comparação que realizamos por meio de operadores

"""
Igualdade ==
Diferença !=
maior que >
menor que <
maior ou igual que >=
menor ou igual que <=
"""
x = 10

y = 5

igualdade =  x == y


#print(igualdade)

#print(type(igualdade))
diferenca = x != y
#print(diferenca)
maior_que = x > y
"""
x > y 
10 > 5 True
"""
#print(maior_que)

menor_que = x < y
"""
10 < 5 False
"""
#print(menor_que)


maior_igual = x >= y
"""
x <= y True or False
x < y True 
x == y False
"""
#print(maior_igual)

menor_igual = x <= y

"""
x <= y -> x < y or x == y
False False
"""
#print(menor_igual)



#operador booleano 
#operadores lógicos 
#AND OR NOT 

#AND -> ADITIVO = QUE TODAS AS SUBEXPRESSÕES DEVEM SER TRUE PARA PODER TER O RESULTADO TRUE

aditivo = (x < y) and (y <= x)
#False and True
#print(aditivo)

#OR -> ALTERNATIVO => A EXPRESSÃO SERÁ TRUE SE AO MENOS 1 DAS SUBEXPRESSOES FOR TRUE

alternativa = (x < y) or (y <= x)
#false or true
#print(alternativa)
#not
expressao = (x < y)

#print(expressao)

negacao_expressao = not (x < y)

#print(negacao_expressao)

x = 60


"""
if (x == 50):# false
# verifica se x == 50, se for True ele executa o bloco de instruções, se for false ele ignora
    #print("X é igual a 50")
else:
    print("x é diferente de 50")
"""


"""
if sempre fica no inicio(sempre terá uma expressão booleana)

elif (deve ter uma expressão booleana)

else(sempre estará no final, e não tem expressão booleana)
"""

if x == 50:
    print("Os valores são iguais")
elif x > 50:
    print("X é maior")
elif x < 50:
    print("X é menor")
else:
    print("NDA Nenhuma das alternativas")




