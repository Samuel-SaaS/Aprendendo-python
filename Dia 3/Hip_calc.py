import math as mt
print('a)Cateto')
print('b)hipotenusa')
e = input('Escolha oque você deseja achar')
match e:
    case 'a':
        c1 = float(input('Digite o valor de um cateto: '))
        h1 = float(input('Digite o valor da hipotenusa: '))
        c2 = mt.sqrt(mt.pow(h1, 2) - mt.pow(c1, 2))
        # c2 = mt.sqrt(mt.pow((h1 - c1), 2)), 
        # Pq não dá certo ↑?, quer dizer, eu sei , mas como eu resolvo???? e se eu separar?
        # Separando deu.
        # Diferença de quadrados, funciona, vô tentar normal
        print(f'O valor do seu cateto é {c2}')
    case 'b':
        c1 = float(input('Digite o valor de um cateto: '))
        c2 = float(input('Digite o valor do outro cateto: '))
        h1 = mt.sqrt(mt.pow(c1, 2) + mt.pow(c2, 2))
        # h1 = mt.sqrt((c1 + c2)(c1 + c2)) # Agr assim não vai, pq?? // entendi, sou bobo, achei que era a mesma coisa da diferença de quadrados, sou bobo
        print(f'O valor da hipotenusa do triangulo é {h1}')
    case _:
        print('Escolha uma alternativa entre a ou b.')