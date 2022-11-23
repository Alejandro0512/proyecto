#PROYECTO
#el programa va a constar de la realizacion de un codigo el cual apartir de preguntas saber que carro se puede comprar con los gustos y presupuestos del ususario
RED = "\033[3;31m"
YELLOW = "\033[3;33m"
GREEN = "\033[3;32m"
PURPLE = "\033[3;35m"
CYAN = "\033[3;36m"
WHITE = "\033[3;37m"
BLUE = "\033[3;34m"

I = 4

print ("BIENVENIDO")
print("________________________________________________________________________")
print("")
print(RED+ "B"+ "\033[0m")
print(YELLOW+ "I"+ "\033[0m")
print(GREEN+ "E"+ "\033[0m")
print(PURPLE+ "N"+ "\033[0m")
print(CYAN+ "V"+ "\033[0m")
print(WHITE+ "E"+ "\033[0m")
print(BLUE+ "N"+ "\033[0m")
print(RED+ "I"+ "\033[0m")
print(YELLOW+ "D"+ "\033[0m")
print(GREEN+ "O"+ "\033[0m")
print("")
print("________________________________________________________________________")
print("")
print ("BIENVENIDO AL CONSESIONARIO KINGDOM NOS COMPLACE QUE NOS HA ELEGIDO")
print("")
print("POR FAVOR ANTES DE SEGUIR QUEREMOS SABER SI ES USTED UN MAYOR DE EDAD ")
print("¿ES USTED UN MAYOR DE EDAD?")
print("")
print( RED+"1."+ "\033[0m"+ "Si"+"\033[0m")
print("")
print( RED+"2."+ "\033[0m"+ "No"+"\033[0m")
print("")
type = pdesicion = int(input())
print("")
print("________________________________________________________________________")
print("")
if (pdesicion == 2 ): 
  print ("SU RESPUSTA A SIDO: 2.No ")
  print ( RED + "ESTA PAGINA ES PARA MAYORES DE EDAD" +"\033[0m" )
  print ( "LO ESPERAMOS PRONTO ")
if (pdesicion == 1):
    print ("SU RESPUESTA A SIDO: 1.Si ")
    print (BLUE+ "NOS ALEGRA QUE NOS HALLAS ELEGIDO :) "+"\033[0m")
    print("")
    print("________________________________________________________________________")
    print("") 
    print ("")
    print ("LAS MARCAS QUE TENEMOS DISPONIBLES SON:  ")
    print ("")
    print("1.chevrolet")
    print("2.Renault")
    print("3.Nissan")
    print("4.Mazda")
    print("5.Kia")
    print("6.Toyota")
    print("7.Volkswagen")
    print("0.Ninguno")
    print("")
    print("DIGITE EL NUMERO DE LA MARCA QUE DESEA COTIZAR")
    type = marca = int(input())
    print("")
    if (marca == 1):
       print("")
       print("CHEVROLET")
       print("")
       print("QUE DESEA: ")
       print("")
       print("1.Camioneta")
       print("2.Automovil")
       print("")
       type = C1 = int(input())
       C1 = (C1*2)%2
       if (C1 == 0):
          print("")
          print(GREEN + "TENEMOS DISPONIBLES"+"\033[0m")
          print("")
          print("TENEMOS DISPONIBLES CON LOS SIGUIENTES COLORES: ")
          print("")
          print("BLANCO, NEGRO Y GRIS")
          COLOR = input("ESCRIBA EL COLOR QUE DESEA")
          print("EL COLOR QUE ESCOGIO FUE: ",COLOR)
          print("")
          print("PARA CONTINUAR EL PROCESO REMITASE AL SIGUIENTE LINK, Y NO SE LE OLVIDE QUE VIENE DE PARTE DE KINGDOM")
          print("")
          print("EL LINK ES EL SIGUIENTE: ")
          print("https://www.chevrolet.com.co/?ppc=GOOGLE_700000001312999_71700000061981839_58700005569261049_p72662396500&gclid=Cj0KCQiAg_KbBhDLARIsANx7wAxQ-tl_dfts2KWsK3EOmXnAOLlYFi1ztW8UeUG3-3m2SEUMT_l1BEQaAh-6EALw_wcB&gclsrc=aw.ds")
    else:
          print (RED +"!LA OPCION DIGITADA NO ES VALIDA!"+ "\033[0m")
          print("DIGITE UNA OPCION VALIDA")
    while (C1 != 0 ):
          print("")
          type = C1 = int(input())
          I = I - 1 
          print("TE QUEDAN ", I , " INTENTOS" )

if (I == 0):
    print(RED + "SE ACABARON EL NUMERO DE INTENTOS"+"\033[0m")
    print("")
    print("POR FAVOR REGRESAR MAS TARDE A VISITARNOS.")
    print("___________________________________________________________________________________________________________________________")
    if (marca == 2):
       print("")
       print("RENAULT")
       print("")
       print("QUE DESEA: ")
       print("")
       print("1.Camioneta")
       print("2.Automovil")
       print("")
       type = R2 = int(input())
       R2 = (R2*2)%2
       if (R2 == 0):
          print("")
          print(GREEN + "TENEMOS DISPONIBLES"+"\033[0m")
          print("")
          print("TENEMOS DISPONIBLES CON LOS SIGUIENTES COLORES: ")
          print("")
          print("BLANCO, NEGRO Y ROJO")
          COLOR = input("ESCRIBA EL COLOR QUE DESEA")
          print("EL COLOR QUE ESCOGIO FUE: ",COLOR)
          print("")
          print("PARA CONTINUAR EL PROCESO REMITASE AL SIGUIENTE LINK, Y NO SE LE OLVIDE QUE VIENE DE PARTE DE FREEDOM")
          print("")
          print("EL LINK ES EL SIGUIENTE: ")
          print("https://www.renault.com.co/?ORIGIN=sea_defensive&CAMPAIGN=co-es-r-l-def-brand-all_products-crossenergy-go-classic-marca-renault&gclid=Cj0KCQiAg_KbBhDLARIsANx7wAzESW0gIBxVU34z_6r08ffhR-FOa6RRDqf9VXb75LGRfvks6faukO4aAtp2EALw_wcB&gclsrc=aw.ds")
    else:
          print (RED +"!LA OPCION DIGITADA NO ES VALIDA!"+ "\033[0m")
          print("DIGITE UNA OPCION VALIDA")
    while (R2 != 0 ):
          print("")
          type = R2 = int(input())
          I = I - 1 
          print("TE QUEDAN ", I , " INTENTOS" )
if (I == 0):
    print(RED + "SE ACABARON EL NUMERO DE INTENTOS"+"\033[0m")
    print("")
    print("POR FAVOR REGRESAR MAS TARDE A VISITARNOS.")
    print("___________________________________________________________________________________________________________________________")
    if (marca == 3):
       print("")
       print("NISSAN")
       print("")
       print("QUE DESEA: ")
       print("")
       print("1.Camioneta")
       print("2.Automovil")
       print("")
       type = N3 = int(input())
       N3 = (N3*2)%2
       if (N3 == 0):
          print("")
          print(GREEN + "TENEMOS DISPONIBLES"+"\033[0m")
          print("")
          print("TENEMOS DISPONIBLES CON LOS SIGUIENTES COLORES: ")
          print("")
          print("BLANCO Y ROJO")
          COLOR = input("ESCRIBA EL COLOR QUE DESEA")
          print("EL COLOR QUE ESCOGIO FUE: ",COLOR)
          print("")
          print("PARA CONTINUAR EL PROCESO REMITASE AL SIGUIENTE LINK, Y NO SE LE OLVIDE QUE VIENE DE PARTE DE FREEDOM")
          print("")
          print("EL LINK ES EL SIGUIENTE: ")
          print("https://www.nissan.com.co/vehiculos/catalogos.html?dcp=psn-aon-all-adw-text-brandexacta_catalogos-co_rg&gclid=Cj0KCQiAg_KbBhDLARIsANx7wAy-jGOt0WOih6fVu5MXcpbSffPnpuckRGESu9IHsY6hUWJmTdWdbBwaAiW6EALw_wcB")
    else:
          print (RED +"!LA OPCION DIGITADA NO ES VALIDA!"+ "\033[0m")
          print("DIGITE UNA OPCION VALIDA")
    while (N3 != 0 ):
          print("")
          type = N3 = int(input())
          I = I - 1 
          print("TE QUEDAN ", I , " INTENTOS" )
    if (I == 0):
        print(RED + "SE ACABARON EL NUMERO DE INTENTOS"+"\033[0m")
        print("")
        print("POR FAVOR REGRESAR MAS TARDE A VISITARNOS.")
    print("___________________________________________________________________________________________________________________________")
    if (marca == 4):
       print("")
       print("MAZDA")
       print("")
       print("QUE DESEA: ")
       print("")
       print("1.Camioneta")
       print("2.Automovil")
       print("")
       type = M4 = int(input())
       M4 = (M4*2)%2
       if (M4 == 0):
          print("")
          print(GREEN + "TENEMOS DISPONIBLES"+"\033[0m")
          print("")
          print("TENEMOS DISPONIBLES CON LOS SIGUIENTES COLORES: ")
          print("")
          print("BLANCO, NEGRO Y GRIS")
          COLOR = input("ESCRIBA EL COLOR QUE DESEA")
          print("EL COLOR QUE ESCOGIO FUE: ",COLOR)
          print("")
          print("PARA CONTINUAR EL PROCESO REMITASE AL SIGUIENTE LINK, Y NO SE LE OLVIDE QUE VIENE DE PARTE DE FREEDOM")
          print("")
          print("EL LINK ES EL SIGUIENTE: ")
          print("https://www.mazda.com.co/?utm_source=Google_SEM&utm_medium=CPCAON&utm_campaign=AON_MARCA&gclid=Cj0KCQiAg_KbBhDLARIsANx7wAy2Vebbz1ObIjnKFQD0D7IVfSTXVAxtpGg-9CoXKY2ah9LT4sw2O1YaAoRKEALw_wcB")
    else:
          print (RED +"!LA OPCION DIGITADA NO ES VALIDA!"+ "\033[0m")
          print("DIGITE UNA OPCION VALIDA")
    while (M4 != 0 ):
          print("")
          type = M4 = int(input())
          I = I - 1 
          print("TE QUEDAN ", I , " INTENTOS" )
if (I == 0):
    print(RED + "SE ACABARON EL NUMERO DE INTENTOS"+"\033[0m")
    print("")
    print("POR FAVOR REGRESAR MAS TARDE A VISITARNOS.")
    print("___________________________________________________________________________________________________________________________")
    if (marca == 5):
       print("")
       print("KIA")
       print("")
       print("QUE DESEA: ")
       print("")
       print("1.Camioneta")
       print("2.Automovil")
       print("")
       type = K5 = int(input())
       K5 = (K5*2)%2
       if (K5 == 0):
          print("")
          print(GREEN + "TENEMOS DISPONIBLES"+"\033[0m")
          print("")
          print("TENEMOS DISPONIBLES CON LOS SIGUIENTES COLORES: ")
          print("")
          print("NEGRO Y ROJO")
          COLOR = input("ESCRIBA EL COLOR QUE DESEA")
          print("EL COLOR QUE ESCOGIO FUE: ",COLOR)
          print("")
          print("PARA CONTINUAR EL PROCESO REMITASE AL SIGUIENTE LINK, Y NO SE LE OLVIDE QUE VIENE DE PARTE DE FREEDOM")
          print("")
          print("EL LINK ES EL SIGUIENTE: ")
          print("https://metrokia.co/?utm_source=google&utm_medium=cpc&utm_campaign=metrokia_website&utm_content=kia_motors&utm_term=metrokia&gclid=Cj0KCQiAg_KbBhDLARIsANx7wAxFKLxa9sa8HWKuX8CokUVyproRb2sGsRkKbowONh3KW7USDCO4uYcaAnMzEALw_wcB")
    else:
          print (RED +"!LA OPCION DIGITADA NO ES VALIDA!"+ "\033[0m")
          print("DIGITE UNA OPCION VALIDA")
    while (K5 != 0 ):
          print("")
          type = K5 = int(input())
          I = I - 1 
          print("TE QUEDAN ", I , " INTENTOS" )
if (I == 0):
    print(RED + "SE ACABARON EL NUMERO DE INTENTOS"+"\033[0m")
    print("")
    print("POR FAVOR REGRESAR MAS TARDE A VISITARNOS.")
    print("___________________________________________________________________________________________________________________________")
    if (marca == 6):
       print("")
       print("TOYOTA")
       print("")
       print("QUE DESEA: ")
       print("")
       print("1.Camioneta")
       print("2.Automovil")
       print("")
       type = T6 = int(input())
       T6 = (T6*2)%2
       if (T6 == 0):
          print("")
          print(GREEN + "TENEMOS DISPONIBLES"+"\033[0m")
          print("")
          print("TENEMOS DISPONIBLES CON LOS SIGUIENTES COLORES: ")
          print("")
          print("BLANCO, NEGRO Y GRIS")
          COLOR = input("ESCRIBA EL COLOR QUE DESEA")
          print("EL COLOR QUE ESCOGIO FUE: ",COLOR)
          print("")
          print("PARA CONTINUAR EL PROCESO REMITASE AL SIGUIENTE LINK, Y NO SE LE OLVIDE QUE VIENE DE PARTE DE FREEDOM")
          print("")
          print("EL LINK ES EL SIGUIENTE: ")
          print("https://www.toyota.com.co/campanas-preventivas-servicio/?https://www.toyota.com.co/campanas-preventivas-servicio/&gclid=Cj0KCQiAg_KbBhDLARIsANx7wAzjYPSZNVBo9Tf48L5qPIHfIF5Xd7YowDeSysT4IfTfoQPZ3s1QTBkaAub0EALw_wcB")
    else:
          print (RED +"!LA OPCION DIGITADA NO ES VALIDA!"+ "\033[0m")
          print("DIGITE UNA OPCION VALIDA")
    while (T6!= 0 ):
          print("")
          type = T6 = int(input())
          I = I - 1 
          print("TE QUEDAN ", I , " INTENTOS" )
if (I == 0):
    print(RED + "SE ACABARON EL NUMERO DE INTENTOS"+"\033[0m")
    print("")
    print("POR FAVOR REGRESAR MAS TARDE A VISITARNOS.")
    print("___________________________________________________________________________________________________________________________")
    if (marca == 7):
       print("")
       print("VOLKSWAGEN")
       print("")
       print("QUE DESEA: ")
       print("")
       print("1.Camioneta")
       print("2.Automovil")
       print("")
       type = V7 = int(input())
       V7 = (V7*2)%2
       if (V7 == 0):
          print("")
          print(GREEN + "TENEMOS DISPONIBLES"+"\033[0m")
          print("")
          print("TENEMOS DISPONIBLES CON LOS SIGUIENTES COLORES: ")
          print("")
          print("BLANCO Y AZUL")
          COLOR = input("ESCRIBA EL COLOR QUE DESEA")
          print("EL COLOR QUE ESCOGIO FUE: ",COLOR)
          print("")
          print("PARA CONTINUAR EL PROCESO REMITASE AL SIGUIENTE LINK, Y NO SE LE OLVIDE QUE VIENE DE PARTE DE FREEDOM")
          print("")
          print("EL LINK ES EL SIGUIENTE: ")
          print("https://www.volkswagen.co/?utm_source=google&utm_medium=cpc&utm_campaign=brand_cpc_ao_sem&utm_content=brand_cpc_ao_sem_keywords&utm_term=brand_cpc_ao_sem_keywords_volkswagen&gclid=Cj0KCQiAg_KbBhDLARIsANx7wAzhgXwycQoef7qtJwUiHkT_jR3HsSNube9Lcc-v8gsgDVeimpa-Q2QaAjdnEALw_wcB")
    else:
          print (RED +"!LA OPCION DIGITADA NO ES VALIDA!"+ "\033[0m")
          print("DIGITE UNA OPCION VALIDA")
    while (V7!= 0 ):
          print("")
          type = V7 = int(input())
          I = I - 1 
          print("TE QUEDAN ", I , " INTENTOS" )
else:
    print("la marca no conincide con ninguna de la lista")
    print("lo retornara al principio")
    
if (I == 0):
    print(RED + "SE ACABARON EL NUMERO DE INTENTOS"+"\033[0m")
    print("")
    print("POR FAVOR REGRESAR MAS TARDE A VISITARNOS.")
    print("___________________________________________________________________________________________________________________________")
    if (marca == 0):
       print("")
       print( BLUE + "GRACIAS POR PASAR A KINGDOM LO ESPERAMOS MUY PRONTO"+"\033[0m")
       print("")
       print("TE ESPERAMOS VUELVE PRONTO ")     
else:
    print (RED +"!LA OPCION DIGITADA NO ES VALIDA!"+ "\033[0m")
    print ( "EN CASO TAL QUE SEA MENOR DE EDAD Y PASAR EL SITIO A UN ADULTO")
    print("")
    print("DIGITAR UNA OPCION VALIDA")
while (pdesicion != 1 ):
    type = pdesicion = int(input())
    I = I - 1 
    print("TE QUEDAN ", I , " INTENTOS" )
    if (I == 0):
        print(RED + "SE ACABARON EL NUMERO DE INTENTOS"+"\033[0m")
        print("")
        print("POR FAVOR REGRESAR MAS TARDE A VISITARNOS.")
        break