# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1018
def greedy(money):
  cells = [100, 50, 20, 10, 5, 2, 1]
  print(money)

  for cell in cells:
    count = money // cell
    money = money % cell
    print('%d nota(s) de R$ %d,00' % (count, cell))
    
          

greedy(576)
greedy(11257)
greedy(503)