ano = int (input(' Digite um ano qualquer: '))
print(30*'+')
print (ano)
print(30*'+')

if (ano%4)==0 and (ano%100)!=0 or (ano%400)==0:
    print ('É ano Bissexto!')
else:
    print (' Não é ano Bissexto!')