v = input('Digite algo: ')
typepri = type(v)
issp = v.isspace()
isn = v.isnumeric()
isal = v.isalpha()
isalfn = v.isalnum()
isup = v.isupper()
islow = v.islower()
iscap = v.istitle()
print('O tipo primitivo desse valor é {}'.format(typepri))
print('Só tem espaços? {}'.format(issp))
print('É um número? {}'.format(isn))
print('É alfabético? {}'.format(isal))
print('É alfanumérico? {}'.format(isalfn))
print('Está em maiúsculas? {}'.format(isup))
print('Está em minúsculas? {}'.format(islow))
print('Está capitalizada? {}'.format(iscap))