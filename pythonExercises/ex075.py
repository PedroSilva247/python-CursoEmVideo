t = []
p = []
for c in range(0, 4):
    n = int(input('Digite um número: '))
    t += [n]
    if n % 2 == 0:
        p += [n]
print(f'Você digitou os valores {t}')
print(f'O valor 9 apareceu {t.count(9)} vezes')
print(f'O valor 3 apareceu na {t.index(3)+1}ª posição' if t.count(3) > 0 else 'O valor 3 não foi digitado')
print(f'Os valores pares digitados foram {p}')