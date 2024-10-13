 # é bem auto-explicativo
 #
 # and → confere se duas ou mais condições são verdadeiras, se alguma não, o resultado será falso
 # or → confere se pelo menos 1 condição é verdadeira
 # not → inverte True para False e False para True
 
peso = 80
 # if peso >= 60 and peso <= 80:
 #   print('Competidor está qualificado')
 # else:
 #   print('Competidor está desqualificado') 
 # if peso <= 60 or peso >= 80:
 #   print('Competidor está desqualificado')
 #else:
 #   print('Competidor está qualificado') 
if not (peso >= 70 and peso <= 90):
     print('Competidor está desqualificado. ')
else:
    print('Competidor está qualificado. ')