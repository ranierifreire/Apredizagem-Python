arroz_kg = 7.00
feijao_KG = 9.00
carne_kg = 35.00

for i in range(3):
  valor = input()
  valor = float(valor)
  if valor <= 10.00:
    print("Posso comprar!")
  else: 
   print("Não compre.")
