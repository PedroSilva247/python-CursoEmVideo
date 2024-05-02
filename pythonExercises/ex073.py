t = ('Palmeiras',
'Internacional',
'Fluminense',
'Corinthians',
'Flamengo',
'Athletico-PR',
'Atlético-MG',
'Fortaleza',
'São Paulo',
'América-MG',
'Botafogo',
'Santos',
'Goiás',
'Bragantino',
'Coritiba',
'Cuiabá',
'Ceará',
'Atlético-GO',
'Avaí',
'Juventude')
p5 = t[0:5]
u4 = t[-4:]
oa = sorted(t)
ps = t.index('Santos') + 1
print(f'''Os 5 primeiros da tabela são {p5}.
Os ultimos 4 da tabela são {u4}
A tabela em ordem alfabetida é {oa}
O Santos está na posição {ps}''')