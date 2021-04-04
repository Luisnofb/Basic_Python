"""
Primeira leva de exercicios em python
"""
print('destinos 1-15')
cezar = int(input('qual opção selecionar:'))

if cezar == 1:
    x = input('escolha um numero:')
    print(f'numero escolhido = {x}')
elif cezar == 2:
    x, y, z = int(input('valor1:')), int(input('valor2:')), int(input('valor3:'))
    print((x+y+z)**2)
elif cezar == 3:
    print('celcius -> fahrenheit'.upper())
    c = float(input('C='))
    f=c*(9.0/5.0)+32.0
    print(f'F={f}')
elif cezar == 4:
    print('km/h -> m/s')
    k= float(input('km/h = '))
    m= k/3.6
    print(f'm/s = {round(m, 2)}')
elif cezar == 5:
    print('Real -> Dolar')
    r = float(input('reais:'))
    cotação = 5.37
    d = r/cotação
    print(f'{round(r,2)} reais são aproximadamente {round(d,2)} dolares.')
elif cezar == 6:
    print('DESCONTOS')
    valor = float(input('valor do produto:'))
    desconto = float(input('desconto(%):'))
    print(f'O valor do produto com o desconto é {valor-(valor*desconto/100)} R$')
elif cezar == 7:
    print('O premio de cada um'.upper())
    amg1 = float(input(' valor dado peolo amigo1:'))
    amg2 = float(input(' valor dado peolo amigo2:'))
    amg3 = float(input(' valor dado peolo amigo3:'))

    premio = float(input('premio:'))
    cartao = amg1+amg3+amg2

    amg1 = amg1 * 100 / cartao;
    amg2 = amg2 * 100 / cartao;
    amg3 = amg3 * 100 / cartao;

    print(f'O amigo1 recebe {round(amg1 * premio / 100, 2)}')
    print(f'O amigo2 recebe {round(amg2 * premio / 100, 2)}')
    print(f'O amigo3 recebe {round(amg3 * premio / 100, 2)}')


else:
    print('Hoi')





