#Johan Santiago Camacho Vargas

MTotal=float(input("¿Cual es el monto total a pagar?\n"))
if MTotal>100000 and MTotal<200000:
    TPago=MTotal*0.9
    print(f"se tuvo un descuento del 10%\nTotal a pagar {TPago}$")
elif MTotal>200000:
      TPago=MTotal*0.8
      print(f"se tuvo un descuento del 10%\nTotal a pagar {TPago}$")
else:
     print(f"no hay descunto\n Total a pagar {MTotal}")