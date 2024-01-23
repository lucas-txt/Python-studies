matrix = []
print('Monte uma matriz de 3 X 3')
for c in range(1, 10):
    if c == 1:
        letra = 'A'
        numero = 1
    elif c == 2:
        letra = 'A'
        numero = 2
    elif c == 3:
        letra = 'A'
        numero = 3  
    elif c == 4:
        letra = 'B'
        numero = 1
    elif c == 5:
        letra = 'B'
        numero = 2
    elif c == 6:
        letra = 'B'
        numero = 3  
    elif c == 7:
        letra = 'C'
        numero = 1
    elif c == 8:
        letra = 'C'
        numero = 2
    elif c == 9:
        letra = 'C'
        numero = 3 
    matrix.append(int(input(f'Digite um valor para [{letra},{numero}]: ')))
print(30*'-=-')
print(f'''\033[32m[  *  ]\033[31m[  A  ][  B  ][  C  ]\033[m
\033[31m[  1  ]\033[m[{matrix[0]:^5}][{matrix[1]:^5}][{matrix[2]:^5}]
\033[31m[  2  ]\033[m[{matrix[3]:^5}][{matrix[4]:^5}][{matrix[5]:^5}]
\033[31m[  3  ]\033[m[{matrix[6]:^5}][{matrix[7]:^5}][{matrix[8]:^5}]''')