"""
Aula 03
"""

#manipulação de strings

a = "Turma TADS 20"

"""
a = "[
        0=> 'T', 
        1 => 'u', 
        2 => 'r', 
        3 => 'm', 
        4 => 'a', 
        5 => ' ', 
        6, 'T' , 
        7 => 'A', 
        8 => 'D', 
        9 => 'S', 
        10 => ' ', 
        11 => '2', 
        12 => '0'
    ]"
"""

#print(a[5])


#Função len() -> utilizada para verificar o tamanho de ums string

#print(len(a))

"""
verificador = ("TADS" in a);

print(verificador)


if(verificador == False):
    print("Dado não encontrado!")
else:
    print("Dado Encontrado")


verficador_dois = ("TA" not in a)

print(verficador_dois)

if(verficador_dois == True):
    print("Esse dado não existe na string principal")
else:
    print("Esse dado existe na string principal")
"""

#b = "Edinelson Luis de Sousa Junior"

#c = (b[10:14])

#print(c)

#d = (b[:14])

#print(d)


#e = (b[2:])

#print(e)


b = "Edinelson Luis de Sousa Junior"


#print(b)


f = (b[0: -6])

#print(f)

#função UPPER -> converte todos os caracteres em caixa alta
maiuscula = b.upper()

#print(maiuscula)


#função lower -> converte todos os caracteres em caixa baixa
minuscula = b.lower()

#print(minuscula)


#Função strip() -> remover espaços em branco de uma string. 

remover_espacos = b.strip()

#print(remover_espacos)


#Função replace() -> substituir um caractere especifico por outro.

substituir_espaco_por_underline = b.replace(" ", "-")

#print(substituir_espaco_por_underline)


frase_motivacional = "Caros amigos, a execução dos pontos do programa agrega valor ao estabelecimento das condições inegavelmente apropriadas. A prática cotidiana prova que a complexidade dos estudos efetuados cumpre um papel essencial na formulação das diretrizes de desenvolvimento para o futuro. Do mesmo modo, a consulta aos diversos militantes promove a alavancagem dos métodos utilizados na avaliação de resultados. Acima de tudo, é fundamental ressaltar que a competitividade nas transações comerciais deve passar por modificações independentemente do impacto na agilidade decisória. Ainda assim, existem dúvidas a respeito de como o novo modelo estrutural aqui preconizado garante a contribuição de um grupo importante na determinação das novas proposições. O que temos que ter sempre em mente é que a constante divulgação das informações facilita a criação das direções preferenciais no sentido do progresso. Por outro lado, a expansão dos mercados mundiais assume importantes posições no estabelecimento de alternativas às soluções ortodoxas. As experiências acumuladas demonstram que a determinação clara de objetivos obstaculiza a apreciação da importância de todos os recursos funcionais envolvidos."


#dados = frase_motivacional.split(" ")

#print(len(dados))

dados = b.split(" ")


print(b)
print(dados)

maiuscula = dados[1]


print(maiuscula.upper())

