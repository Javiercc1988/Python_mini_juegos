################################# IMPORTACION DE MODULOS #################################
import random
import time
import os

################################# DECLARACION DE FUNCIONES DE UTILIDAD #################################

def limpiar_pantalla():     # FUNCION CREADA PARA LIMPIAR LA PANTALLA CON EL MODULO OS
    time.sleep(1)
    os.system("cls")

################################# FUNCIONES DE BIENVENIDA #################################

def bienvenida():
    print(f"""
    
    \t {"-"*80}


    \t   ██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░
    \t   ██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗
    \t   ██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║
    \t   ██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║
    \t   ██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝
    \t   ╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░


    \t{"-"*80}""")

################################# FUNCIONES DE HISTORIA Y PANTALLAS #################################

def historia():
    print("""\n
    Año 2150, tras 100 años desde la gran lucha por los recursos de tierra fértil y agua nos encontramos en una sociedad dominada por la ley del más fuerte donde unos pocos tienen el poder, las armas y los recursos suficientes para someter al resto de supervivientes. Durante estos 100 años han perecido más de 6 mil millones de personas, sus cuerpos abonan las pocas tierras donde ahora se puede cultivar.
    En el planeta existen 2 grandes urbes, las cuales son gobernadas con mano de hierro sometiendo a su sociedad esclavizada racionando el agua y la comida. Su población débil por el incesante trabajo y la falta de alimentos es incapaz de derrocar a un dictador bien protegido.
    El resto de la gente que vive fuera de las urbes conocido como “Logarks” es perseguida por partidas de caza las cuales son extremadamente sangrientas y sádicas. Estas cacerías se retransmiten en tiempo real en las urbes y es el único momento en el cual se deja de trabaja para de esta forma aniquilar cualquier ápice de esperanza por escapar a los montes.
    Los “Logarks” han creado sociedades subterráneas en antiguas minas de hierro a suficiente profundidad como para evitar los escáneres de los drones de combate, de esta forma esta pequeña sociedad sobrevive mientras trata de reunir lo suficiente como para asesinar a los dos grandes inquisidores de las urbes conocidos como “Anukiles”. 
    Los “Anukiles” se reúnen solo una vez al año para realizar el cambio de sangre. Estos descubrieron que si vaciaban sus cuerpos y cambiaban su sangre por el de otro humano joven y totalmente sano sus células sometidas a un alto nivel de rayos UTRE se regeneraban. La gran complicación de esto, era encontrar humanos sanos desde su nacimiento ya que prácticamente la natalidad era nula y los bebes que nacían en su mayoría estaban enfermos.
    \n
    """)

def pantalla1():
    print(f""" \n#################   # 1. EL SECUESTRO   #################\n""")
    print(f"""\n
    Tú como participante activo de las revueltas de los Logarks eras el encargado de ejecutar el plan de secuestrar al donante de este año, y, ¿porque no? si la oportunidad se presenta, de matar a los Anukiles.
    Tras ejecutar un plan un tanto desastroso (algo que cabia esperar ya que se trazo escondidos en minas bajo tierra y sin ninguna tecnología) no obstante efectivo, has conseguido matar a un Anukil, robar un vehículo y secuestrar al donante lo cual ahora te deja en una huida sin freno del otro Anukil y sus guardianes los cuales quieren recuperar al donante, arrancarte la piel a tiras y hacertela comer mientras sigues vivo.
    \n""")

def pantalla2():
    limpiar_pantalla()
    print(f""" \n#################   # 2. LA PRIMERA MINA   #################\n""")
    
    print(f"""\n
    Has conseguido llegar a la primera mina donde podrás cambiar de vehiculo, reponer agua, comida y continuar la huida hasta la base principal donde estará preparada la emboscada si todo sale segun lo previsto podreis matar al Anukil restante y su guardia.
    """)
    
    print(f"""\n
    Comandante de mina: ¡ JODER {nombre} ! llegas con muy poco margen no estamos preparados para repeler a los guardianes rápido carga la cantimplora y el deposito de agua ¡¡RÁPIDO RÁPIDO!!\n
    {nombre}: ¡¡VOY TODO LO RÁPIDO QUE PUEDO DEBERIAIS HABER ESTADO MÁS ATENTOS!!
    """)
    
    time.sleep(1)
    
    print(f"""
    Comandante de mina: {nombre} no dejes que te pillen, pero si lo hacen tendrás que matar al chico no dudes todo depende de ello.\n
    """)

    time.sleep(1)

    print(f"""\n
    Comandante de mina: Buena suerte
    """)

def pantalla3():
    limpiar_pantalla()
    print(f"""\n#################   # 3. LA LLEGADA   #################\n""")
    print(f"""\n
    Comandante general: {nombre} No es posible, creia que no lo conseguirías me alegro de verte eres un maldito heroe.
    Todo esta preparado están apunto de llegar cuando crucen el puente ¡BOOOOM! los cimientos que sugetan el puente caeran sobre la ladera y una avalancha de piedras aplastara a esos malnacidos.
    {nombre}: ¡Comandante ahí llegan, todos preparados!\n
    """)

    for i in range(1,6):    # BUECLE CUENTA ATRÁS PARA EXPLOSION
        print(i,"...")
        time.sleep(1)

    print("\nBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM\n")
    time.sleep(3)
    print("Ha..")
    time.sleep(1)
    print("Ha..?")
    time.sleep(3)
    print("\n",nombre,": Ha ¿¡FUNCIONADO!?\n")
    time.sleep(2)
    print(f"""\n Comandante general: {nombre} si hijo, ha funcionado todo termina aquí gracias a ti.. ¡hemos ganado!""")

def juego_terminado():
    print("""
        
    /t░░░░░██╗██╗░░░██╗███████╗░██████╗░░█████╗░  ████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██████╗░░█████╗░
    /t░░░░░██║██║░░░██║██╔════╝██╔════╝░██╔══██╗  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██╔══██╗██╔══██╗
    /t░░░░░██║██║░░░██║█████╗░░██║░░██╗░██║░░██║  ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░██║██║░░██║
    /t██╗░░██║██║░░░██║██╔══╝░░██║░░╚██╗██║░░██║  ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░██║██║░░██║
    /t╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚█████╔╝  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║██████╔╝╚█████╔╝
    /t░╚════╝░░╚═════╝░╚══════╝░╚═════╝░░╚════╝░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░""")


################################# FUNCIONES DE TURNOS DE JUGADOR E INFORMACIÓN DE ESTADISTICAS #################################

def turno_jugador(estadisticas):
    opciones_jugador = ["Beber","Velocidad controlada","Correr","Descansar y comer","Tu estado"] # LISTA DE OPCIONES JUGADOR
    num_opcion = ["A","B","C","D","E"]      # INDICATIVO A SELECCIONAR POR EL JUGADOR
    distancia_enemigos = [11,12,13,14,15,16,17,18,19,20]  # LISTAS PARA DISTANCIAS ALEATORIAS
    distancia_enemigos_aleatoria = random.randint(1, len(distancia_enemigos))   # CARGAMOS LA DISTANCIA ALEATORIA EN UNA VARIABLE PARA USARLA


    print("\nEstas son tus opciones: \n")
    for i in range(len(opciones_jugador)):  # RECORREMOS E IMPRIMIMOS LA LISTA DE OPCIONES A ELEGIR
        print("\t",num_opcion[i] + "- " + opciones_jugador[i])

    eleccion = input("\n¿Qué opción elijes para salvar tu vida?: ")
    eleccion = eleccion.upper()             # CONVERTIMOS LA ELECCION DEL JUGADOR A MAYÚSCULA SIEMPRE


    while eleccion not in num_opcion:       # SI LA ELECCION NO ESTA EN LAS OPCIONES REPETIMOS LA PREGUNTA
        print("\nElije una opción de las disponibles. ¡Deja de perder el tiempo o te alcanzarán!\n")

        opciones_jugador = ["Beber","Velocidad controlada","Correr","Descansar","Tu estado"]
        num_opcion = ["A","B","C","D","E"]

        print("Estas son tus opciones: \n")
        for i in range(len(opciones_jugador)):  # RECORREMOS E IMPRIMIMOS LA LISTA DE OPCIONES A ELEGIR
            print("\t",num_opcion[i] + ". " + opciones_jugador[i])

        eleccion = input("¿Qué opción elijes para salvar tu vida?: ")
        eleccion = eleccion.upper()


    if eleccion == "A":
        if estadisticas[0][1] == 0: # BEBER AGUA
            print("\n¡No es momento de beber, se acercan!\n")

                #ENEMIGOS
            estadisticas[2][0] += 8 # DISTANCIA ENEMIGOS

        else:
                #JUGADOR
            estadisticas[0][0] += 0     # DISTANCIA JUGADOR
            estadisticas[0][1] = 0      # SED DEL JUGADOR
            estadisticas[0][2] += 10    # HAMBRE DEL JUGADOR
            estadisticas[0][2] += 10    # CANSANCIO

                #VEHICULO
            estadisticas[1][0] -= 10    # GASTO DE COMBUSTIBLE
            estadisticas[1][1] += 10    # AUMENTO DE TEMPERATURA

                #ENEMIGOS
            estadisticas[2][0] += distancia_enemigos_aleatoria    # DISTANCIA ENEMIGOS


    elif eleccion == "B":   # SEGUIR CONDUCIENDO NORMAL
            #JUGADOR
        estadisticas[0][0] += 10    # DISTANCIA JUGADOR
        estadisticas[0][1] += 10    # SED DEL JUGADOR
        estadisticas[0][2] += 10    # HAMBRE DEL JUGADOR
        estadisticas[0][2] += 10    # CANSANCIO

                #VEHICULO
        estadisticas[1][0] -= 10    # GASTO DE COMBUSTIBLE
        estadisticas[1][1] += 10    # AUMENTO DE TEMPERATURA
            
            #ENEMIGOS
        estadisticas[2][0] += distancia_enemigos_aleatoria    # DISTANCIA ENEMIGOS
    
    elif eleccion == "C":   # CORRER
        if estadisticas[1][2] == 0:
            print("\nNo puedes utilizar el turbo el motor esta demasiado resentido\n")

                #ENEMIGOS
            estadisticas[2][0] += 10    # DISTANCIA ENEMIGOS
        
        else:
                #JUGADOR
            estadisticas[0][0] += 40    # DISTANCIA JUGADOR
            estadisticas[0][1] += 20    # SED DEL JUGADOR
            estadisticas[0][2] += 20    # HAMBRE DEL JUGADOR
            estadisticas[0][2] += 20    # CANSANCIO

                        #VEHICULO
            estadisticas[1][0] -= 30    # GASTO DE COMBUSTIBLE
            estadisticas[1][1] += 20    # AUMENTO DE TEMPERATURA
            estadisticas[1][2] -= 1     # GASTO DE TURBOS

                #ENEMIGOS
            estadisticas[2][0] += distancia_enemigos_aleatoria    # DISTANCIA ENEMIGOS

    elif eleccion == "D":   # DESCANSAR Y COMER
            #JUGADOR
        estadisticas[0][0]         # DISTANCIA JUGADOR
        estadisticas[0][1] += 20   # SED DEL JUGADOR
        estadisticas[0][2] = 0     # HAMBRE DEL JUGADOR
        estadisticas[0][2] = 0     # CANSANCIO

            #VEHICULO
        estadisticas[1][0] += 0     # GASTO DE COMBUSTIBLE
        estadisticas[1][1] -= 20    # AUMENTO DE TEMPERATURA

            #ENEMIGOS
        estadisticas[2][0] += distancia_enemigos_aleatoria   # DISTANCIA ENEMIGOS

    elif eleccion == "E":   # TU ESTADO TOTAL
            #JUGADOR
        info_stats(estadisticas)
        time.sleep(5)

            # ENEMIGOS
        estadisticas[2][0]  # DISTANCIA DE LOS ENEMIGOS

def info_stats(estadisticas):
    print(f"""
    {" "*5} \|/     JUGADOR     \|/     |   MILLAS RECORRIDAS: {(estadisticas)[0][0]}   |    SED: {(estadisticas)[0][1]} % -    |   HAMBRE: {(estadisticas)[0][2]} % |   CANSANCIO: {(estadisticas)[0][3]} % 
    {" "*5} \|/     VEHICULO    \|/     |   COMBUSTIBLE: {(estadisticas)[1][0]} %       |    TEMPERATURA: {(estadisticas)[1][1]} % -    |   TURBO: {(estadisticas)[1][2]}
    {" "*5} \|/     ENEMIGOS    \|/     |   DISTANCIA: {(estadisticas)[2][0]} 
    """)

def info_jugador(estadisticas):
    print("Has recorrido",estadisticas[0][0],"millas.")
    print("Los enemigos han recorrido",estadisticas[2][0],"millas.")
    
    if (estadisticas[0][0] - estadisticas[2][0]) < 20:
        print("\n¡¡¡¡¡ Cuidado tienes a los enemigos encima !!!!!\n")

    elif(estadisticas[0][1] >= 70):
        print("\n¡¡¡¡¡ Cuidado si no bebes moriras de sed !!!!!\n")

    elif(estadisticas[0][2] >= 70):
        print("\n¡¡¡¡¡ Cuidado si no comes moriras de hambre !!!!!\n")

    elif(estadisticas[0][3] >= 70):
        print("\n¡¡¡¡¡ Cuidado si no descansas moriras de cansancio !!!!!\n")

def muerte_jugador(estadisticas):   
    if (estadisticas[0][0] - estadisticas[2][0]) <= 0:
        print("\n¡HAS PERDIDO!, Los enemigos te han capturado...\n")
        info_jugador(estadisticas)
        return True

    elif(estadisticas[0][1] >= 100):
        print("\n¡HAS PERDIDO!, has muerto deshidratado...\n")
        info_jugador(estadisticas)
        return True

    elif(estadisticas[0][2] >= 100):
        print("\n¡HAS PERDIDO!, eres literalmente un muerto de hambre...\n")
        info_jugador(estadisticas)
        return True

    elif(estadisticas[0][3] >= 100):
        print("\n¡HAS PERDIDO!, has muerto por cansancio..\n")
        info_jugador(estadisticas)
        return True

################################# FUNCIONES DE EVENTOS #################################

def evento_calentamiento():
    limpiar_pantalla()
    if estadisticas[1][1] > 50:
        print(f"""\n
        ¡¡ NO !!
        ¡NO ES POSIBLE! 
        El coche está fallando ese maldito inútil de Charlie...
        me dijo que estaba perfecto maldita sea tendré que parar a poner agua.. """)
        
                #VEHICULO
        estadisticas[1][0] += 0     # GASTO DE COMBUSTIBLE
        estadisticas[1][1] = 0      # AUMENTO DE TEMPERATURA

                #ENEMIGOS
        estadisticas[2][0] += 25
        print("Los enemigos están a: ",estadisticas[2][0],"millas cada vez están más cerca debo continuar\n")

def evento_lodazal():
    limpiar_pantalla()
    print(f"""\n
    ¡¿JODER NADA VA A SALIRME BIEN HOY?! 
    debo intentar salir de este maldito lodazal si trato de correr demasiado el coche se hundirá y estaré perdido""")
    
            #VEHICULO
    estadisticas[1][0] += 5     # GASTO DE COMBUSTIBLE
    estadisticas[1][1] += 10     # AUMENTO DE TEMPERATURA

            #ENEMIGOS
    estadisticas[2][0] += 15
    print("Los enemigos están a: ",estadisticas[2][0],"millas cada vez están más cerca debo continuar\n")


# _______________________________________________________________________________________
#|                                                                                       |
#|***************************************************************************************|#
#|******************************** LANZAMIENTO DEL JUEGO ********************************|#
#|***************************************************************************************|#
#|_______________________________________________________________________________________|#

fin_juego = False
bienvenida()    # DAMOS LA BIEVENIDA AL JUGADOR
time.sleep(1)

###################### --> VARIABLES <-- ######################

estadisticas = [[0,0,0,0],[100,0,2],[-20]] # 0- JUGADOR(0 MILLAS RECORRIDAS, 1 SED, 02 HAMBRE, 3, CANSANCIO) / 1- VEHICULO (0 COMBUSTIBLE, 1 TEMPERATURA, 2 TURBOS) / 2- ENEMIGOS(0 DISTANCIA)
contador = 0    # CONTADOR PARA INTRODUCIR PANTALLAS O EVENTOS
nombre = input("Introduce tu nombre: ")     # PEDIMOS EL NOMBRE AL JUGADOR
time.sleep(0.5)

###############################################################

print("Hola",nombre)
time.sleep(0.5)

###############################################################
historia()      # CARGAMOS LA HISTORIA
time.sleep(2)
pantalla1()     # CARGAMOS LA PANTALLA 1

while fin_juego == False:
    if contador == 3:
        evento_lodazal()

    elif contador == 5:
        pantalla2()

    elif contador == 8:
        pantalla3()
        fin_juego = True
    else:
        turno_jugador(estadisticas)
        evento_calentamiento()
        info_jugador(estadisticas)
        
    if muerte_jugador(estadisticas):
        fin_juego = True
        break
    contador += 1