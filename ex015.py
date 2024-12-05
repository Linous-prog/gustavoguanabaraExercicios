dia = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?: '))
aluguel = dia * 60 + km * 0.15
    # O dia custa R$60 e R$0.15 por km rodado
print(f'O total a pagar é de {aluguel:.2f}')
