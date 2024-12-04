largura = float(input('Digite a largura da parede: '))
altura  = float(input('Digite a altura da parede: '))
dimensao = largura * altura #Para calcular a área(dimensao) precisamos calcular a largura x altura
tinta = dimensao / 2 # Para calcular a quantidade de tinta dividimos a dimensão por 2
print(f'Sua parede tem a Dimensão de {largura:.2f} x {altura:.2f} e sua área é de {dimensao:.3f}m2')
print(f'Para pintar essa parede, Você precisará de {tinta} Litros de tinta')