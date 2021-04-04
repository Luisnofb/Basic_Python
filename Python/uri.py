# -*- coding: utf-8 -*-
"""
simple algorithms from URI

"""

print('Informe os valores:'.upper())
a,b,c = float(input(' A=')),float(input(' B=')),float(input(' C='))
triangulo= a*c/2
circulo = 3.14159*(c**2)
trap = (a+b)*c/2
quad =b**2
ret =a*b
print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {quad:.3f}')
print(f'RETANGULO: {ret:.3f}')