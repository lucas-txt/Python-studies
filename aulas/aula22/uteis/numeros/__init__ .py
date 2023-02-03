def fatorial(n):
    tot = 1
    for c in range(1, n+1):
        tot *= c
    return tot

# num = int(input('Digite um numero: '))
# print(fatorial(num))