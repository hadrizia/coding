# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

def multiples(a, b):
    if a % b == 0 or b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
    
a, b = input().split()
a = int(a)
b = int(b)
multiples(a, b)

