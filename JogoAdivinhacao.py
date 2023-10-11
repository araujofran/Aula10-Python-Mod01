import random

num = random.randint (0,5)

adivinha = int(input('escolha um numero de 0 a 5:    ' ))

print(adivinha)

if adivinha==num:
   print('Parabéns você acertou!')
else:
   print ('Você ERROUUUUU! kkkkk ')

print ('Obrigado por participar! O número sorteado foi: {}'.format(num))





