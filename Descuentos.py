#Calculadora de Descuentos
#Luis Santiafo Cubillos 
prc = int(input("Ingrese el precio del total de tu compra\n"))
if prc >0 and prc<100000:
    print ("No hay descuento")
elif prc >=100000 and prc <200000:
    print ("Tienes un descuento del 10%")
    print ("El total a pagar es: ", prc - (prc * 0.10))
elif prc >=200000 :
    print ("Tienes un descuento del 20%")
    print ("El total a pagar es: ", prc - (prc * 0.20))
else :
    print ("Precio invalido.")

