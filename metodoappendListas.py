#Programa que cria listas para a organização de equipamentos adquiridos por uma empresa
organizacao=[]
resposta="S"
while resposta=="S":
  organizacao.append(input("Equipamento: "))
  organizacao.append(float(input("Valor: ")))
  organizacao.append(int(input("Número Serial: ")))
  organizacao.append(input("Departamento: "))
  resposta=input("Digite S para continuar: ").upper()