#Johan Santiago Camacho Vargas
#Correcion de codigo 2

num=1                       #<-no habia error aqui pero queria simplificar el nombre
suma_pares=0

while num<=20:              #<-solo faltaba el "<="
    if num % 2 ==0:         #<-el numero que habia que poner era 0
        suma_pares+=num     #<-no habia error aque pero se podia evitar repetir cosas con el "+="
    num+=1                  #<-solo faltaba esto para evitar un bucle infinito

print(f"La suma de los numeros pares del 1 al 20 es : {suma_pares}")

#se podria hacer de una manera mas simple, pero solo me pidieron corregirlo asi que asi queda