# -*- coding: utf-8 -*-
from scipy import log2

a=float(input("podaj zadana czestotliwosc: "))
while a!=(-1):
	b=float(input("podaj wyjsciowa czestotliwosc: "))
	print(1200*log2(b/a))
	a=float(input("podaj zadana czestotliwosc: "))