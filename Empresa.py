import importe 
i = int ( input ("Ingrese el numero del producto que desea conocer\n 1. Camisa \n 2. Pantalon \n 3. Zapatos \n"))
if i == 1 :
    print ("Escogiste la mejor opcion ! \n Nuestras camisas cuentan con un precio estandar de $15.99 \n Y en los siguientes colores : \n - Negro \n -Blanco \n Azul oscuro \n Beige")
elif 2 :
   print ("Escogiste la mejor opcion ! \n Nuestros pantalones cuentan con un precio estandar de $19.99 \n Y en los siguientes colores : \n - Negro \n Verde oscuro \n Azul oscuro\n Azul clado")
elif 3 : 
   print ("Escogiste la mejor opcion ! \n Nuestros zapatos cuentan con un precio estandar de $25.99 \n Y en los siguientes colores : \n - Negro \n -Blanco \n Azul oscuro \n Beige")
else :
   print ("Error 404")
print ("\n Ahora,en tu lista de compra,elige la cantidad de productos de cada tipo que quieres comprar\n")
ctn = int (input ("Cuantos camisas quiere comprar? \n"))
ctn2 = int (input ("Cuantos pantalones quiere comprar? \n"))
ctn3 = int (input ("Cuantos zapatos quiere comprar? \n"))
ctnr = ctn + ctn2 + ctn3 
if ctnr >10 :
   print ("Al comprar mas de 10 de nuestro catalogo de productos,te vamos a hacer un 10% de descuento")

else:
   print (float (f"El total a pagar es{(ctn*15.99)+(ctn2+19.00) +{ctn3*25.99}}"))