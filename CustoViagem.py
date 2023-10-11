distancia = int (input (' Qual a distância percorrida da viagem? '))
print ('-'*20)
print (distancia,'km')
print ('-'*20)
if distancia <=200:

    custoViagem = distancia * 0.50

    print (' O custo da viagem será de R$ {:.2f}.'.format(custoViagem))

else:   
    custoViagem = distancia * 0.45

    print (' O custo da viagem será de R$ {:.2f}.'.format(custoViagem))
print ('-'*20)
print ('Tenha uma boa viagem!!!')
print ('-'*20)