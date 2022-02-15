
codigo, numeroPecas, valorUnitario = input().split(" ")  # pega 3 valores na mesma linha e atribui a variáveis

# Converte o valor para os tipos necessários
codigo = int(codigo)
numeroPecas = int(numeroPecas)
valorUnitario = float(valorUnitario)

codigoDois, numeroPecasDois, valorUnitarioDois = input().split(" ")

codigoDois = int(codigoDois)
numeroPecasDois = int(numeroPecasDois)
valorUnitarioDois = float(valorUnitarioDois)

totalPago = (numeroPecas * valorUnitario) + (numeroPecasDois * valorUnitarioDois)

print("VALOR A PAGAR: R$ %.2f" % totalPago)
