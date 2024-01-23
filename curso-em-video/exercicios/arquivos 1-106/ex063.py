print(30*'-')
print('Sequencia de Fibonacci')
print(30*'-')
n = int(input('Quantos termos você quer ver? ')) #numero
c = 0 #contador
t1 = 0 #termo um
t2 = 1 #termo dois
print('{} > {} >'.format(t1, t2), end=' ')
while c <= n-3:
    termo = t1 + t2
    print('{} >'.format(termo), end=' ')
    t1 = t2
    t2 = termo
    c += 1
print('fim')
