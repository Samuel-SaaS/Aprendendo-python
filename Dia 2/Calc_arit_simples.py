n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
o1 = input('Digite uma operação (+, -, *, /, **, // ou %)')

match o1:
    case '+':
        print(n1+n2)
    case '-':
        print(n1-n2)
    case '*':
        print(n1*n2)
    case '**':
        print(n1**n2)
    case '/':
        if n2 == 0:
            print('Não é possível dividir por 0. ')
        else:
            print(n1/n2)
    case '//':
        if n2 == 0:
            print('Não é possível dividir por 0. ')
        else:
            print(n1//n2)
    case '%':
        if n2 == 0:
            print('Não é possível dividir por 0. ')
        else:
            print(n1%n2)
    case _:
        print('Digite uma operação válida. ')
