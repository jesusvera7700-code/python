ACROSTICO_DB = {
    'A': 'Amor',
    'B': 'Bondad',
    'C' : 'Cuidado',
    'D' : 'Determinación',
    'E' : 'Emocionante',
    'F' : 'Esperanza',
    'G' : 'Fortaleza'  ,
    'H' : 'Honestidad',
    'I' :  'Ilusión',
    'J' : 'Jubilo',
    'K' : 'Karma',
    'L' : 'Lealtad',
    'M' : 'Magico',
    'N' : 'Nobleza',
    'O' :'Optimismo',
    'P' : 'Paz',
    'Q' : 'Química',
    'R' : 'Resiliencia',
    'S' : 'Sabiduría',
    'T' : 'Ternura',
    'U' : 'Unión',
    'V' : 'Valor',
    'W' : 'Wiskas',
    'X' : 'X',
    'Y' : 'Yantra',
    'Z' : 'Zen'
        }
num = 0
plb = input ("Ingrese la palabra para el acrostico\n") .strip() .upper() 
print ("-"*30)
print (f"La palabra es {plb}")
print ("Letra      Palabra")
for indice,plb in enumerate(plb):
   palabra_asig = ACROSTICO_DB.get(plb, " ")
   print (f"{plb}       {palabra_asig}")
if __name__ == "__main__":
 print ("-"*30,"\n Te quedo bonito w")

