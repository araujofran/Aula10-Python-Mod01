from datetime import date
ano = int (input(' \033[0;31;40mDigite um ano qualquer: '))
if ano == 0:
    ano = date.today().year
    print (ano)
if (ano%4)==0 and (ano%100)!=0 or (ano%400)==0:
    print ('\033[32mÉ ano Bissexto!'.format(ano))
else:
    print (' \033[33;40mNão é ano Bissexto!'.format(ano))