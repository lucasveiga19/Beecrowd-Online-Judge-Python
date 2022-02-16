
A, B, C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

areaTriangulo = (A * C) / 2
print("TRIANGULO: %.3f" % areaTriangulo)

areaCirculo = 3.14159 * (C * C)
print("CIRCULO: %.3f" % areaCirculo)

areaTrapezio = ((A + B)/2) * C
print("TRAPEZIO: %.3f" % areaTrapezio)

areaQuadrado = B * B
print("QUADRADO: %.3f" % areaQuadrado)

areaRetangulo = A * B
print("RETANGULO: %.3f" % areaRetangulo)
