n = int(input('Digite um número: '))
c = int(input('''Deseja continuar?
[0] SIM
[1] NÃO
Digite: '''))
print(40*'-')
s = n
maior = n
menor = n
qn = 1
while c == 0:
    n = int(input('Digite um número: '))
    c = int(input('''Deseja continuar?
[0] SIM
[1] NÃO
Digite: '''))
    print(40 * '-')
    s += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    qn += 1
m = s / qn
print('Média: {}'.format(m))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
