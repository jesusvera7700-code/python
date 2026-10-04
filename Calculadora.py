op= int (input("Seleccione la operación\n 1.Suma \n 2.Resta \n 3.Multiplicación\n 4. División\n"))
num1 = float(input("Pon el primer numero a operar\n"))
num2 = float(input("Pon el segudo numero a operar\n"))
if op >0 and num2 != 0 and op <=4 :  
    OPERACIONES = {
        0 : 'Programa Cerrado',
        1 : (f'Resultado : {num1+num2}'),
        2 : (f'Resultado : {num1-num2}'),
        3 : (f'Resultado : {num1*num2}'),
        4 : (f'Resultado : {num1/num2}'),
        }
    if op >=0 and op <=4 :
        res = OPERACIONES.get(op)
        print (f"{res}")
else:
    print ("Error ")