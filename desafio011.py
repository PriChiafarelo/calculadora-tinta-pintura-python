"""Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados"""

altura = float(input('Digite a altura da parede: '));
largura = float(input('Digite a largura da parede: '));

print('A quantidade de tinta necessária para pintar {} m2 é de {} litros'.format((altura * largura), (altura * largura)/2));
