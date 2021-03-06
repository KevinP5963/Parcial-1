RAM=20.00
descuento=0.60
Estado=int(input("identifique el estado de la memoria 1=si es nueva y 0=si es usada "))
if Estado==1:
   print("la memoria RAM es nueva el precio es: ",RAM)
   cantidad=int(input("ingrese cuantas Memorias compraran: "))
   total1= RAM*cantidad
   print("el precio total es de: ",total1)
if Estado==0:
   print("la memoria RAM es usada se le reducira el 60%")
   Cantidad1=int(input("indique la cantidad que compraran: "))
   descuento1= RAM*descuento
   print("el precio de la memoria con descuento es de: ",descuento1)
   total2= Cantidad1*descuento1
   print("el precio total es de: ",total2)


   