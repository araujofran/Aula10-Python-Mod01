n1= int(input('Digite um numero: '))
n2= int(input('Digite um numero: '))
n3= int(input('Digite um numero: '))

if n1>n2 and n1>n3:
    print (' O numero {} é maior que {} e {}!'.format(n1,n2,n3))
elif n2>n1 and n2>n3:
     print (' O numero {} é maior que {} e {}!'.format(n2,n1,n3))
else:
      print (' O numero {} é maior que {} e {}!'.format(n3,n2,n1))