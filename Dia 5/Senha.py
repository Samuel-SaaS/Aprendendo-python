# Construa um user
# username não deve possuir mais que 12 caracteres
# username não deve possuir menos que 6 caracteres
# username não deve possuir espaço (' ')
# username não deve possuir números (1, 2, 3, ...)

nome = input('Digite seu nome de usuário: ')
a = nome.isalpha()
b = len(nome)
if a == True and b >= 6 and b < 12:
    print(f'Bem-vindo, {nome}!')
else:
    print('Sua senha não foi aceita')
    
    
# Também é possível usando nome.algumacoisa:

nome = input('Digite seu nome de usuário: ')
a = len(nome)
b = nome.find(' ')
c = nome.find('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0')

if a > 12 or a < 6:
    print('Sua senha não corresponde com a quantidade de letras necessárias, entre 6 a 12. ')
elif not b == -1:
    print('Seu nome de usuário não pode conter espaços')
elif not c == -1:
    print('Seu nome de usuário não pode conter digitos')
else:
    print(f'Bem-vindo {nome}')
