# jeito sem import

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
r = (a ** 2 + b ** 2) ** (1 / 2)
print(f'A hipotenusa vai medir {r:.2f}')



# importando ficaria mais facil :
from math import hypot

c = float(input('Comprimento do cateto oposto: '))
d = float(input('Comprimento do cateto adjacente: '))
hi= hypot(c, d)
print(f'A hipotenusa vai medir {hi:.2f}')