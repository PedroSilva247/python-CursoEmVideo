# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer, {:-^20}!'.format(nome))
# < alinhado a esquerda
# > alinhado a direita
# ^ alinhado ao centro
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))

# Quebrar linha no meio do print: \n
# Não quebrar a linha no final do print: end=' '
# {:.3f} = limite de 3 casas decimais flutuantes