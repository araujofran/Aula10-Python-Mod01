a= float(input('Digite um numero: '))
b= float(input('Digite um numero: '))
c= float(input('Digite um numero: '))

print (a,b,c)
# Formúla (b-c<a<b+c) 2 ands = True ( Triangulo) 

# b-c menor que a = ( True) e a menor b+c = True 

if ((b-c)<a) and (a<(b+c)):
    print ('É triangulo')
else:
    print (' Não é Triangulo!')