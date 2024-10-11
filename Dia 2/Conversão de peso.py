o1 = float(input('Digite o valor da temperatura atual'))

print('Escolha a medida atual: ')
print('a)Celsius ')
print('b)Fahrenheit ')
print('c)Kelvin ')
t1 = input('Digite a letra correspondente a sua medida: ')

print('Escolha a medida atual: ')
print('a)Celsius ')
print('b)Fahrenheit ')
print('c)Kelvin ')
t2 = input('Digite a letra correspondente a sua escala desejada: ')

match t1, t2:
    case 'a', 'a':
        print(f'sua medida de °C para °C é {o1}')
    case 'a', 'b':
        cf = (5*o1 - 160)/9
        print(f'Sua temperatura de °C para °F é {cf}')
    case 'a', 'c':
        ck = o1 + 273
        print(f'Sua temperatura de °C para °K é {ck}')
    case 'b', 'a':
        fc = (9*o1 + 160)/5
        print(f'Sua temperatura de °F para °C é {fc}')
    case 'b', 'b':
        print(f'sua medida de °F para °F é {o1}')
    case 'b', 'c':
        fk = (5/9)*(o1-32) + 273
        print(f'sua medida de °F para °K é {fk}')
    case 'c', 'a':
        kc = o1 - 273
        print(f'Sua temperatura de °K para °C é {kc}')
    case 'c', 'b':
        kf = (9/5)*(o1-273) + 32
        print(f'Sua temperatura de °K para °F é {kf}')
    case 'c,', 'c':
        print(f'sua medida de °K para °K é {o1}')
    case _:
        print('Digite uma letra entre a, b ou c')

    # Tem alguma coisa errada, não sei oque é
