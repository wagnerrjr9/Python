'''Faça um programa que leia 4 notas bimestrais de um__a disciplina, calcule e mostre a média aritmética do
bimestre'''
import time
n1 = int(input('Digite a nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))
media = (n1+n2+n3+n4) /4
print(f'A sua média é {media:.1f}')