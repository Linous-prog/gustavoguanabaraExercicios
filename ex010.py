real = float(input('Quanto de dinheiro você tem na carteira? R$:'))
dolar = real / 6.04 # Para converter a moeda é so dividir pelo preço dela
yen =  real / 0.040
euro = real / 6.35
print(f"Com {real:.2f} reais você pode comprar US${dolar:.2f} Dólares , ou {yen:.2f}iens, ou {euro:.2f}Euros" )
