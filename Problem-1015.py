
X1, Y1 = input().split(" ")
X2, Y2 = input().split(" ")

X1 = float(X1)
X2 = float(X2)
Y1 = float(Y1)
Y2 = float(Y2)

distancia = pow(pow(X2 - X1, 2) + pow(Y2 - Y1, 2), 1/2)

print("%.4f" % distancia)
