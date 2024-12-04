preco = float(input('Qual é o preço do produto? R$:'))
x = preco - (preco * 15 / 100)
print(f'O produto que custava {preco:.2f} na promoção com desconto de 15%, vai custar R${x:.2f}.')