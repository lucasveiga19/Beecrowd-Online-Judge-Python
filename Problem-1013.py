
A, B, C = input().split(" ")

A = int(A)
B = int(B)
C = int(C)

maior = A
if B > maior:
    maior = B
if C > maior:
    maior = C

print(maior, "eh o maior")
