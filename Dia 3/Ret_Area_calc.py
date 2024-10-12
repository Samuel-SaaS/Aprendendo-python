import math as mt
import tkinter as tk
print('Escolha qual a forma do plano: ')
print('a> Quadradi')
print('b)Triangulo')
print('c)trapézio')
print('d)circulo')
print('e)hexagono')
f = input('Digite qual letra corresponde a sua forma: ')
match f:
    case 'a':
        h = float(input('Digite a altura do quadrado em cm: '))
        b = float(input('Digite a base do quadrado em cm: '))
        aq = abs(h*b)
        print(f'A área é igual a {aq}cm^2')
    case 'b':
        h = float(input('Digite a altura do triangulo em cm: '))
        b = float(input('Digite a base do triangulo em cm: '))
        at = abs((h*b)/2)
        print(f'A área é igual a {at}cm^2')
    case 'c':
        h = float(input('Digite a altura do quadrado em cm: '))
        B = float(input('Digite a base maior do trapézio em cm: '))
        b = float(input('Digite a medidad da base maior do trapézio: '))
        atr = abs(((B + b)*h)/2)
        print(f'A área é igual a {atr}cm^2')
    case 'd':
        r = float(input('Defina o valor do raio: '))
        r = mt.pow(r, 2)
        pi = mt.pi
        ac = abs(pi*r)
              
        print(f'A área é igual a {ac}cm^2')
    case 'e':
        l = float(input('Digite o valor do seu lado'))
        ah = (3*l**2*mt.sqrt(3))/2
        print(f'A área é igual a {ah}cm^2')
 # Até agr só aprendi sobre importar esse math no chute, foi bem útil, vi um cabra usando um tal de tkinter e tentei ver se tinha algum outro pra usar raiz e elevar sem **
