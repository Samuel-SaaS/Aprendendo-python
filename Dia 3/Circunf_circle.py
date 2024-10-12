import math
r = float(input('Digite o valor do raio da circunferência: '))
pi = math.pi
c = round(2*pi*r, 2)
print(f'O valor da circunferência do seu circulo é {c}')
#hmmmm, descobri q dá pra arredondar pra qnts números decimais(x) eu quiser se eu usar round('', x)