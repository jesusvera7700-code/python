print ("="*50,"\nTecnico Superior-Notas\n","="*50)
usr = input("Escriba su nombre  de usuario \n")
nt=200
while nt >100 or nt <0:
 nt=int(input("Cual es tu nota?\n"))
 if nt >=90 and nt <101:
    print (f"Excelente,{usr} vas muy bien,sigue asi!")
 elif nt >=70 and nt<90 :
   print(f"Aprobado,{usr} felicitaciones,aunque puedes mejorar...")
 elif nt >0 and nt<70:
  print(f"Reprobado,{usr} mejora o vete.")
 else :
  print (f"{usr} deberias aprender a leer")
