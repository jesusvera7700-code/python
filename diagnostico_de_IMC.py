#Johan Santiago Camacho Vargas
#Correcion de codigo 1

peso=70.5
altura=1.75

imc=peso/altura**2       #Correccion de formula

if imc<18.5:        #faltaba ":"
    print("Diagnostico: Peso bajo")
elif imc>=18.5 and imc<30:                  #dos errores, faltaba poner un "=" y no tine logica creer que una divicion tenga que dar un numero exacto (24.9), es mejor poner un rango
    print("Diagnostico: Peso normal")       
elif imc>=30:                               #otro error de logica, ponia un "<" en lugar de un ">", lo que ocaciona que no de el resultado correctamente
    print("Diagnostico: Sobrepeso")
else:
     print("Diagnostico: Obecidad")   

#se puede mejorar mas, pero la instrucciones no lo dicen asi que asi queda