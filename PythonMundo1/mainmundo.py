""" import math
n = float(input('Digite um número Real: '))
n = math.floor(n)
print('O número Inteiro desse Real é {}!'.format(n))
 """
""" import math
c1 = float(input('Digite o tamanho do cateto oposto em cm: '))
c2 = float(input('Digite o tamanho do cateto adjacente em cm: '))
hip = (pow(c1, 2) + pow(c2, 2))**(1/2)
print('O tamanho da hipotenusa é de {:.2f} cm!'.format(hip))
 """
""" import math
n = float(input('Digite um ângulo em graus: '))
n = n * math.pi / 180
s = math.sin(n)
c = math.cos(n)
t = math.tan(n)
print('Seu sen={:.2f}; cos={:.2f}; tg={:.2f}!'.format(s, c, t))
 """
""" 
import random
a = str(input('Qual o nome do primeiro aluno? '))
b = str(input('Qual o nome do segundo aluno? '))
c = str(input('Qual o nome do terceiro aluno? '))
d = str(input('Qual o nome do quarto aluno? '))
e = [a, b, c, d]
random.shuffle(e)
print('A ordem que os alunos vão apresentar é: {}, {}, {} e {}!'
      .format(e[0], e[1], e[2], e[3]))
 """
import pygame
pygame.init()
pygame.mixer.music.load('abc.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
