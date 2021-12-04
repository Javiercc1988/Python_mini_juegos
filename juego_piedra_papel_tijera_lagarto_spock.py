import random

def buscar_aleatorio(lista):
    palabra = random.randint(0, len(lista))
    return lista[palabra]


############# CREO UNA FUNCION PARA CADA OPCION
def piedra(palabra):
    if palabra == "Piedra":
        if eleccion_maquina == "Piedra":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Piedra contra piedra es... EMPATE!")
            
        elif eleccion_maquina == "Papel":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Papel envuelve piedra, ¡PIERDES!")
            
        elif eleccion_maquina == "Tijera":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Piedra aplasta Tijera, ¡GANAS!")
            
        elif eleccion_maquina == "Lagarto":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Piedra aplasta Lagarto, ¡GANAS!")
            
        else:
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Spock vaporiza Piedra, ¡PIERDES!")



def papel(palabra):
    if palabra == "Papel":
        if eleccion_maquina == "Papel":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Papel contra Papel es... EMPATE!")
            
        elif eleccion_maquina == "Piedra":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Papel envuelve piedra, ¡GANAS!")
            
        elif eleccion_maquina == "Tijera":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Tijera corta Papel, ¡PIERDES!")
            
        elif eleccion_maquina == "Lagarto":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Lagarto devora papel, ¡PIERDES!")
            
        else:
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Papel desautoriza Spock, ¡GANAS!")

            

def tijera(palabra):
    if palabra == "Tijera":
        if eleccion_maquina == "Tijera":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Tijera contra Tijera es... EMPATE!")
            
        elif eleccion_maquina == "Piedra":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Piedra aplasta Tijera, ¡PIERDES!")
            
        elif eleccion_maquina == "Papel":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Tijera corta Papel, ¡GANAS!")
            
        elif eleccion_maquina == "Lagarto":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Tijera decapita Lagarto, ¡GANAS!")
            
        else:
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Spock rompe Tijera, ¡PIERDES!")
            

def lagarto(palabra):
    if palabra == "Lagarto":
        if eleccion_maquina == "Lagarto":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Lagarto contra Lagarto es... EMPATE!")
            
        elif eleccion_maquina == "Piedra":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Piedra aplasta Lagarto, ¡PIERDES!")
            
        elif eleccion_maquina == "Tijera":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Tijera decapita Lagarto, ¡PIERDES!")
            
        elif eleccion_maquina == "Papel":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Lagarto devora papel, ¡GANAS!")
            
        else:
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Lagarto envenena Spock, ¡GANAS!")


def spock(palabra):
    if palabra == "Spock":
        if eleccion_maquina == "Spock":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Spock contra Spock es... EMPATE!")
            
        elif eleccion_maquina == "Piedra":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Spock vaporiza Piedra, ¡GANAS!")
            
        elif eleccion_maquina == "Tijera":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Spock rompe Tijera, ¡GANAS!")
            
        elif eleccion_maquina == "Lagarto":
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Lagarto envenena Spock, ¡PIERDES!")
            
        else:
            print(nombre,", ha elegido",decision)
            print(oponente,", ha elegido",eleccion_maquina)
            print("Papel desautoriza Spock, ¡PIERDES!")



            

###################################################################################################
################################# P R O G R A M A #################################################
###################################################################################################

#### CREAMOS LA LISTA DE OPCIONES
lista_palabras = ["Piedra","Papel","Tijera","Lagarto","Spock"]
#### CREAMOS LA LISTA DE CONTRINCANTES
lista_oponentes = ["Tamagochi","Son Goku","Lisa simpson","Sheldon Cooper","Una lata de cocacola","Jhon wick","Morty","Anatoli Kárpov","J.C. Van damme"]

eleccion_maquina = buscar_aleatorio(lista_palabras)
oponente = buscar_aleatorio(lista_oponentes)

#### LA VARIABLE REPETIR NOS SIRVE PARA EL BUCLE WHILE
repetir = True

#### SOLICITAMOS EL NOMBRE AL USUARIO
nombre = input("Introduce tu nombre: ").capitalize()


########################### EMPIEZA EL JUEGO
print("¡Hola!,",nombre)
jugar = input("\n¿Quieres jugar?(S/N): ").lower()


while repetir:
        #### SI EL USUARIO QUIERE JUGAR
    if jugar == "s":
        
        #### USAMOS LA FUNCION RANDOM PARA ELEGIR UN OPONENTE DIFERENTE CADA VEZ
        eleccion_maquina = buscar_aleatorio(lista_palabras)
        
        #### USAMOS LA FUNCION RANDOM PARA ELEGIR UNA OPCION DEL OPONENTE CADA VEZ
        oponente = buscar_aleatorio(lista_oponentes)
        
        print("\nVas a jugar contra...",oponente)
        eleccion_maquina #### HACEMOS LA ELECCIÓN DE LA MAQUINA
        decision = input("\n¿Que opción quieres?\nPiedra\nPapel\nTijera\nLagarto\nSpock\n: ").capitalize()
        print()
            #### EJECUTAMOS LAS FUNCIONES SI LA DECISION ELEGIDA ESTA EN LA LISTA DE OPCIONES
        if decision in lista_palabras:
            piedra(decision)
            papel(decision)
            tijera(decision)
            lagarto(decision)
            spock(decision)
        else:
            ### MARCAMOS UN ERROR AL NO ELEGIR ALGO VALIDO
            print("¡Error no has dicho la palabra mágica!")
            repetir = True
    else:
        ### NOS DESPEDIMOS PORQUE EL JUGADOR NO QUIERE JUGAR
        print("Otro dia será, ¡adios!")

### AL TERMINAR PREGUNTARMOS SI QUEREMOS JUGAR OTRA PARTIDA
    jugar = input("\n¿Quieres jugar otra partida?(S/N): ").lower()
    if jugar == "s":
        repetir = True
    else:
        repetir = False
        print("El juego ha terminado, ¡adios!")
        
    
