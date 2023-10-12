from datetime import date
ano = int (input(' Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year
    print (ano)
if (ano%4)==0 and (ano%100)!=0 or (ano%400)==0:
    print ('É ano Bissexto!'.format(ano))
else:
    print (' Não é ano Bissexto!'.format(ano))