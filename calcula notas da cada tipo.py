def calcular_notas(preco):
  """
  Calcula a menor quantidade de notas para pagamento de um produto.

  Argumentos:
    preco: O preço do produto (inteiro).

  Retorno:
    Um dicionário com a quantidade de notas de cada valor.
  """

  notas = {
      100: 0,
      50: 0,
      20: 0,
      10: 0,
      5: 0,
      2: 0,
      1: 0
  }

  # Verifica se o preço é suficiente para nota de 100
  if preco >= 100:
    notas[100] = preco // 100
    preco -= notas[100] * 100

  # Verifica se o preço é suficiente para nota de 50
  if preco >= 50:
    notas[50] = preco // 50
    preco -= notas[50] * 50

  # Continua verificando para cada valor de nota
  if preco >= 20:
    notas[20] = preco // 20
    preco -= notas[20] * 20

  if preco >= 10:
    notas[10] = preco // 10
    preco -= notas[10] * 10

  if preco >= 5:
    notas[5] = preco // 5
    preco -= notas[5] * 5

  if preco >= 2:
    notas[2] = preco // 2
    preco -= notas[2] * 2

  # Resto (se houver) será em notas de 1
  notas[1] = preco

  return notas

# Lê o preço do produto
preco = int(input("Digite o preço do produto: "))

# Calcula a quantidade de notas
notas = calcular_notas(preco)

# Exibe o resultado
for valor_nota, quantidade_nota in notas.items():
  if quantidade_nota > 0:
    print(f"Quantidade de notas de R${valor_nota}: {quantidade_nota}")
