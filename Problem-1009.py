
vendedor = str(input())
salarioFixo = float(input())
totalVendas = float(input())

totalRecebido = salarioFixo + (totalVendas * 0.15)

print("TOTAL = R$ %.2f" % totalRecebido)
