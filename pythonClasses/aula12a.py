nome = input('Qual é seu nome? ')
if nome == 'Pedro':
    print('Que nome bonito!')
elif nome == 'Gustavo' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino')
    
print('Tenha um bom dia, {}!'.format(nome))