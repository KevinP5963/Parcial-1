barreno=112
sierra=75
ventaA=int(input("ingrese el numero de barrenos vendidos: "))
ventaB=int(input("ingrese el numero de sierras vendidas: "))
pesoA=ventaA*barreno
print("el peso total de la venta de barrenos es de: ",pesoA)
pesoB=ventaB*sierra
print("el peso total de la venta de sierras es de: ",pesoB)
pesoTotal=pesoA+pesoB
print("el peso total del paquete que sera enviado es de: ",pesoTotal)