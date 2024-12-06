from math import cos, sin, tan, radians

h1 = int(input('Digite o Ângulo que voce deseja: '))
seno = sin(radians(h1))
coseno = cos(radians(h1))
tang = tan(radians(h1))
print(f'O Ângulo de {h1} tem o SENO de {seno:.2f}')
print(f'O Ângulo de {h1} tem o COSSENO de {coseno:.2f}')
print(f'O Ângulo de {h1} tem a TANGENTE de {tang:.2f}')