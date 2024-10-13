peso = float(input('Digite o seu peso: '))
print('a)gramas')
print('b)Quilogramas')
print('c)Toneladas')
print('d)Libras')
un1 = input('Escolha a alternativa que corresponde a unidade do peso informado: ')
print('a)gramas')
print('b)Quilogramas')
print('c)Toneladas')
print('d)Libras')
un2 = input('Escolha a alternativa que corresponde a unidade do peso que deseja converter: ')

match un1, un2:
    case 'a', 'b':
        c = round(peso/1000, 2)
        print(f'O peso convertido é: {c}kg')
    case 'a', 'c':
        c = round(peso/1000000, 2)
        print(f'O peso convertido é: {c}t')
    case 'a', 'd':
        c = round(peso*0.0022, 2)
        print(f'O peso convertido é: {c}lb')
    case 'b', 'a':
        c = round(peso*1000, 2)
        print(f'O peso convertido é: {c}g')
    case 'b', 'c':
        c = round(peso/1000, 2)
        print(f'O peso convertido é: {c}t')
    case 'b', 'd':
        c = round(peso*2.2, 2)
        print(f'O peso convertido é: {c}lb')
    case 'c', 'a':
        c = round(peso*1000000, 2)
        print(f'O peso convertido é: {c}g')
    case 'c', 'b':
        c = round(peso*1000, 2)
        print(f'O peso convertido é: {c}kg')
    case 'c', 'd':
        c = round(peso*2204.62, 2)
        print(f'O peso convertido é: {c}lb')
    case 'd', 'a':
        c = round(peso*453.59, 2)
        print(f'O peso convertido é: {c}g')
    case 'd', 'b':
        c = round(peso*0.45, 2)
        print(f'O peso convertido é: {c}kg')
    case 'd', 'c':
        c = round(peso*0.00045 , 2)
        print(f'O peso convertido é: {c}t')
    case _:
        print('Digite uma alternativa válida entre a, b, c ou d')