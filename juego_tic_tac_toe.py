import random


#### FUNCION PARA UN NUMERO ALEATORIO QUE SERÁ LA ELECCION DE LA MAQUINA
def aleatorio(board):
    numero = random.randint(1, len(board)-1)
    while (str(numero).isdigit()==False):
        numero = random.randint(1, len(board)-1)
    return numero


#### CREAMOS EL TABLERO CON UNA LISTA QUE NUMERA CADA UNO DE LOS HUECOS
def tablero(board):
    print(("+"+"-"*7)*3, end="+\n")
    print(("|"+" "*7)*3, end="|\n")
    print("|" + " "*3 + board[1] + " "*3 + "|" + " "*3 + board[2] + " "*3 + "|" + " "*3 + board[3] + " "*3,end="|\n")
    print(("|"+" "*7)*3, end="|\n")
    print(("+"+"-"*7)*3, end="+\n")
    print(("|"+" "*7)*3, end="|\n")
    print("|" + " "*3 + board[4] + " "*3 + "|" + " "*3 + board[5] + " "*3 + "|" + " "*3 + board[6] + " "*3,end="|\n")
    print(("|"+" "*7)*3, end="|\n")
    print(("+"+"-"*7)*3, end="+\n")
    print(("|"+" "*7)*3, end="|\n")
    print("|" + " "*3 + board[7] + " "*3 + "|" + " "*3 + board[8] + " "*3 + "|" + " "*3 + board[9] + " "*3,end="|\n")
    print(("|"+" "*7)*3, end="|\n")
    print(("+"+"-"*7)*3, end="+\n")

#### TURNO DEL JUGADOR, LO METEMOS EN UN BUCLE WHILE CUANDO EL JUGADOR INTRODUCE UN NUMERO SE COMPRUEBA SI ESTÁ
#### EN EL RANGO DE LOS NUMEROS DE LA LISTA, SI NO SE MANDA UN MENSAJE DE ERROR Y SE VUELVE A PEDIR
#### LUEGO COMPROBAMOS QUE LA CASILLA ESTA LIBRE, SI NO ES ASÍ VOLVEMOS A PEDIR UN NUMERO AL JUGADOR
#### Y POR ULTIMO AÑADIMOS EL NUMERO A LA LISTA DE LAS CASILLAS YA ELEGIDAS Y CAMBIAMOS EL NUMERO DEL TABLERO POR EL SIMBOLO DEL JUGADOR.
def turno_jugador():
    repeticion_turno = True
    
    while repeticion_turno:
        turno_jugador = int(input("¿Donde quieres poner ficha?: "))

        if turno_jugador > 0 and turno_jugador < 10:
            print("Has elegido la posicion",turno_jugador,"\n")
            repeticion_turno = False
        else:
            print("¡El rango introducido no es correcto!\n")
            repeticion_turno = True
       
        if turno_jugador in num_elegidos:
            print("La casilla ya está utilizada")
            repeticion_turno = True
        else:
            num_elegidos.append(turno_jugador)
            board2[turno_jugador] = "O"
            repeticion_turno = False

    return turno_jugador


#### TURNO DE LA MAQUINA, IGUAL QUE EN EL JUGADOR COMPROBAMOS QUE EL RANGO DE NUMEROS ES EL CORRECTO
#### SI EL NUMERO ALEATORIO DE LA MAQUINA YA ESTA COGIDO EN EL TABLERO VOLVEMOS A TIRAR OTRO ALEATORIO
#### AÑADIMOS EL NUMERO ELEGIDO A LA LISTA DE NUMEROS YA GASTADOS Y MARCAMOS LA CASILLA EN EL TABLERO CON EL SIMBOLO "X" DE LA MAQUINA
def turno_maquina():

    turno_maquina = aleatorio(board)

    if turno_maquina > 0 and turno_maquina < 10:
        print("La máquina ha elegido",turno_maquina)
    else:
        empezar = True

    if turno_maquina in num_elegidos:
        turno_maquina = aleatorio(board)
        while turno_maquina in num_elegidos:
            turno_maquina = aleatorio(board)
            
        num_elegidos.append(turno_maquina)
        board2[turno_maquina] = "X"
        
    else:
        num_elegidos.append(turno_maquina)
        board2[turno_maquina] = "X"
        
    return turno_maquina
    

#### AQUI CREAMOS LAS POSIBLES COMBINACIONES GANADORAS PARA CIRCULO, SI NINGUNA SE CUMPLE DEVOLVEMOS UN GANAR FALSE
def gana_circulo(board2):
    
    if board2[1] == board2[2] == board2[3] == "O":
        ganar = True
        return ganar
    elif board2[4] == board2[5] == board2[6] == "O":
        ganar = True
        return ganar
    elif board2[7] == board2[8] == board2[9] == "O":
        ganar = True
        return ganar
    elif board2[1] == board2[4] == board2[7] == "O":
        ganar = True
        return ganar
    elif board2[2] == board2[5] == board2[8] == "O":
        ganar = True
        return ganar
    elif board2[3] == board2[6] == board2[9] == "O":
        ganar = True
        return ganar
    elif board2[1] == board2[5] == board2[9] == "O":
        ganar = True
        return ganar
    elif board2[3] == board2[5] == board2[7] == "O":
        ganar = True
        return ganar
    else:
        ganar = False
        return ganar

#### AQUI CREAMOS LAS POSIBLES COMBINACIONES GANADORAS PARA 'X', SI NINGUNA SE CUMPLE DEVOLVEMOS UN GANAR FALSE
def gana_x(board2):
    
    if board2[1] == board2[2] == board2[3] == "X":
        ganar = True
        return ganar
    elif board2[4] == board2[5] == board2[6] == "X":
        ganar = True
        return ganar
    elif board2[7] == board2[8] == board2[9] == "X":
        ganar = True
        return ganar
    elif board2[1] == board2[4] == board2[7] == "X":
        ganar = True
        return ganar
    elif board2[2] == board2[5] == board2[8] == "X":
        ganar = True
        return ganar
    elif board2[3] == board2[6] == board2[9] == "X":
        ganar = True
        return ganar
    elif board2[1] == board2[5] == board2[9] == "X":
        ganar = True
        return ganar
    elif board2[3] == board2[5] == board2[7] == "X":
        ganar = True
        return ganar
    else:
        return False


### TEXTO PARA EMPATE
def empate():
    largo_lista = len(num_elegidos)
    if largo_lista == 9:
        print("""\n
                ███████╗███╗░░░███╗██████╗░░█████╗░████████╗███████╗
                ██╔════╝████╗░████║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                █████╗░░██╔████╔██║██████╔╝███████║░░░██║░░░█████╗░░
                ██╔══╝░░██║╚██╔╝██║██╔═══╝░██╔══██║░░░██║░░░██╔══╝░░
                ███████╗██║░╚═╝░██║██║░░░░░██║░░██║░░░██║░░░███████╗
                ╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝\n""")
        
        
### TEXTO PARA GANAR
def ganador1():
    print("""\n
                ██╗░░██╗░█████╗░░██████╗  ░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░██╗██╗
                ██║░░██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██║██║
                ███████║███████║╚█████╗░  ██║░░██╗░███████║██╔██╗██║███████║██║░░██║██║░░██║██║██║
                ██╔══██║██╔══██║░╚═══██╗  ██║░░╚██╗██╔══██║██║╚████║██╔══██║██║░░██║██║░░██║╚═╝╚═╝
                ██║░░██║██║░░██║██████╔╝  ╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝╚█████╔╝██╗██╗
                ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝╚═╝\n""")


### TEXTO CUANDO GANA MAQUINA
def perdedor():
    print("""\n
                ██╗░░██╗░█████╗░░██████╗  ██████╗░███████╗██████╗░██████╗░██╗██████╗░░█████╗░░░░░░░░░░
                ██║░░██║██╔══██╗██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗░░░░░░░░░
                ███████║███████║╚█████╗░  ██████╔╝█████╗░░██████╔╝██║░░██║██║██║░░██║██║░░██║░░░░░░░░░
                ██╔══██║██╔══██║░╚═══██╗  ██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║██║░░██║██║░░██║░░░░░░░░░
                ██║░░██║██║░░██║██████╔╝  ██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝╚█████╔╝██╗██╗██╗
                ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░╚════╝░╚═╝╚═╝╚═╝\n""")



####################################################################
                ##  P  R  O  G  R  A  M  A  ##
####################################################################

    
### CREAMOS LA LISTA PARA LAS CASILLAS DEL TABLERO
board = ["0","1","2","3","4","5","6","7","8","9"]
### CREO UNA COPIA DE LA LISTA PARA PODER MODIFICARLA Y QUE EL TABLERO VAYA CAMBIANDO
board2 = board[:]
### LOS NUMEROS QUE SE ELIGEN SE AÑADEN A ESTA LISTA PARA PODER COMPROBAR SI SE REPITEN CELDAS EN ALGUNA ELECCION DE CADA TURNO
num_elegidos = []
### IMPRIMO EL TABLERO ORIGINAL
tablero(board)
### CREO LA FUNCION PARA QUE ENTRE EL BUCLE WHILE Y EMPIECE EL JUEGO
empezar = True


while empezar:

    tablero(board2)
    jugador = turno_jugador()
    gana_jugador = gana_circulo(board2)
    empatados = empate()
    maquina = turno_maquina()
    gana_maquina = gana_x(board2)

    
    if gana_jugador == True:
        ganador1()
        empezar = False
    elif gana_maquina == True:
        perdedor()
        empezar = False
    elif empatados == True:
        empate()
        empezar = False
    else:
        continue

    tablero(board2)



