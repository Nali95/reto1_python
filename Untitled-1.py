'''print ("HOLA Julian")
print ("TE AMO")
'''

def CDT (usuario, capital, tiempo):
    '''
    usuario = int(input("ingrese nombre del usuario:"))
    capital = int(input("ingrese monto a ingresar:"))
    tiempo = int(input("ingrese tiempo del CDT")
    '''
    if tiempo>2:
        valor_int = (capital*0.03*tiempo)/12
        valor_total = valor_int + capital
        print (valor_total)
    elif tiempo<2:
        valor_per = (capital*0.02)
        valor_total = capital - valor_per
        print (valor_total)
    return "para el usuario", usuario, "la cantidad de dinero a recibir, según el monto inicial ", capital, "para un tiempo de", tiempo, "meses es:",  valor_total
usuario = str(input("introdusca el nombre del usuario"))

CDT(usuario,1000000,3)
CDT(usuario,6500000,2)
        
        