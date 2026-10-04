productos=["Aceite 3L","Arroba de arroz","Espagueti 200gr","Mantequilla 250gr","Azucar 2.5kg","Panela 1kg","Arina de trigo 1kg"]
precio=[35000,47000,2200,17000,9000,8000,4000]
suma=0;decicion="s"
print("bienvenido a la tienda\nLos productos son los siguientes:\n")

#Ciclo de compra (o nose como llamarlo)

while decicion.upper()=="S":
    for i in range (7):                                     #Esto lo aprendi en PSeInt, con esto evito tener que escribir linea por linea
        print({i+1},productos[i],"-"*20,precio[i],"$")
    NumProd=int(input("\n¿Que producto decea comprar?\n"))  
    if NumProd<8 and NumProd > 0: 
        for i in range (7):                                     #nose como se me ocurrio esto pero funciona, repite y compara 7 veces para decidir cual es la suma
            if NumProd==i+1:
                can=int(input("¿que cantidad?\n"))
                suma=suma+(precio[i]*can)
                decicion=input("¿Quiere llevar otro producto?\n(S,N)\n")          #pregunta para repetir o no 
                print("="*60,"\n")
    else:
        print("\nEste producto no existe,vuelva a intentar\n")                    #por si alguien se le da por poner algun numero que no este en la lista 

#Salida de los precios

if suma >100000:
    print(f"el total es {suma}$,pero por haber gastado mas de 100000 tuvo un descuento del 10%\ntotal a pagar: {suma*0.9}$\n")
elif suma>200000:
    print(f"el total es {suma}$,pero por haber gastado mas de 200000 tuvo un descuento del 10%\ntotal a pagar: {suma*0.8}$\n")
else:
    print(f"El total a pagar es de {suma}$\n")