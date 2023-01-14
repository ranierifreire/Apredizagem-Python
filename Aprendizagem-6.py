# ************************************************************
# # a = int(input('Digite um valor:  '))
# # b= int(input('Segundo valor:  '))
# # resto_a = a % 2
# # resto_b = b % 2
# # if resto_a == 0 or not resto_b == 0:
# #     print('Os Número digitado é par')
# # else: 
# #     print('Nenhum número par foi digitado')

# *********************************************************

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro Valor: '))

if a > b and a > c: 
    print('O maior número é: {}'.format(a))
elif b > a and b > c:
    print('O maior número é: {}'.format(b))
else: 
    print('O maior número é: {}'.format(c))
