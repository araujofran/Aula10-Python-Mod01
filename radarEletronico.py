velocidade = int(input(' Velocidade registrada na foto: '))
print(10*'-')
print (velocidade)
print(10*'-')
if velocidade >= 80:
    print ('Multa Otário kkkk')
    valorMulta = (velocidade-80)*7
    print (' O valor da multa é de R${}'.format(valorMulta))

else:
    print ('Ufa tá tudo tranquilo sem multa')

print(10*'-')
