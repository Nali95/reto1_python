def CDT (usuario:str, capital:int, tiempo:int): 
    if tiempo>2:
        valor_int = (capital*0.03*tiempo)/12
        valor_total = valor_int + capital
    else:
        valor_per = capital*0.02
        valor_total = capital - valor_per
        #mensaje = "Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, según el monto inicial: " + str(capital)+ " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total)
    #mensaje = (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial: {capital} para un tiempo de {tiempo} meses es: {valor_total}")
    #return mensaje
    return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}'

#prueba   
usuario1 = str(input("introduzca el nombre del usuario"))
capital= int(input("introduzca el monto del CDT"))
tiempo= int(input("introduzca el tiempo del CDT"))
print (CDT(usuario1,capital,tiempo))
#print (CDT(usuario2,5000000,2))
