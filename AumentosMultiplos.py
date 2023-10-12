print(60*'-')

salario =float (input ('Qual é o seu salário? R$ '))

print(60*'-')
if salario > 1250:
    nsal= (salario * 1.10)
   
    print('Seu salario de R$ {:.2f} tera uma aumento  e será R$ {:.2f}'.format (salario, nsal))
    
else:
    nsal= (salario * 1.15)
   
    print('Seu salario de R$ {:.2f} tera uma aumento  e será R$ {:.2f}'.format (salario, nsal))
    
print(60*'-')
print ('Bom Trabalho!!!')
print(60*'-')