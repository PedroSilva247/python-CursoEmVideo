import random
t = []
for c in range(0, 5):
    n = random.randint(1, 10)
    t += [n]
print(end=''f"Os valores sorteados foram:")
menor = sorted(t)[0]
maior = sorted(t)[-1]
for c in t:
    print(end=' 'f'{c}')
print(f'''
O maior valor sorteado foi {maior}''')
print(f'O menor valor sorteado foi {menor}')