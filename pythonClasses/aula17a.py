num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # adiciona o elemento na ultima posição
num.sort() # ordena os valores de forma crecente
num.sort(reverse=True) # ordena os valores de forma decrecente
num.insert(2, 0) # insere, na posição 2, o valor 0
num.pop() # remove o ultimo elemento
num.pop(3) # remove o elemento da posição 3
num.remove(2) # remove o primeiro elemento de valor 2 e da erro se nao houver nenhum
len(num) # quantos elementos tem na lista
print(num)