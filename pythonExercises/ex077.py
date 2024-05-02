vogais = []
palavras = ['aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar']
for p in palavras:
    vogais = []
    for le in str(p):
        if le in 'aeiou':
            vogais += le
    print(end=''f'Na palavra {p.upper()} temos')
    for v in vogais:
        print(end=' 'f'{v.upper()}')
    print()
