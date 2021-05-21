import turtle

objeto = turtle.Turtle()

"""
para andar para frente => objeto.fd(tamanho)
para andar para trás => objeto.bk(tamanho)
para andar para o lado esquerdo => objeto.lt(angulo)
para andar para o lado direito => objeto.rt(angulo)
"""
#parâmetros de desenho

for i in range(0, 3):
    objeto.fd(100)
    objeto.rt(120)
    i=+1


#fim dos parâmetros
#função que irá executar na tela 
turtle.mainloop()