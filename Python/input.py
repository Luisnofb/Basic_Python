"""
Recebendo dados do usuário :)
"""
# Entrada de dados
print('fala teu nome ai parça:')
nome = input()
# Saida de dados
"""
print("\noi {0}".format(nome))
#achei..
print('oi',nome)
"""
#atual
print(f'oi {nome}')
idade = input('qual sua idade?')#poderia ser int(input())
print(f'{nome} nasceu em {2021 - int(idade)}')
