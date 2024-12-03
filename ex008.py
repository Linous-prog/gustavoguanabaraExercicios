d = float(input('Uma distância em metros: '))
km = d / 1000 # Para saber a quantidade de kilômetros
hm = d / 100 # Para saber a quantidade de Hectômetros
dam = d / 10 # Para saber a quantidade de Decâmetros
dm = d * 1 # Para saber a quantidade de Decímetros
cm = d * 100 # Para saber a quantidade de centímetros
mm = d * 1000 # Para saber a quantidade de milímetros

print(f'A medida de {d}m corresponde a \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm:.0f}cm \n{mm:.0f}mm')
