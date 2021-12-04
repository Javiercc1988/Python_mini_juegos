import readchar, os
from random import randint

############################## | FUNCIONES | ##############################

def random_objects_in_map(list_objects, num_objects, MAP_WIDTH, MAP_HEIGHT):
    ### GENERAMOS DE FORMA AUTOMATICA OBJETOS POR EL MAPA PASANDOLE UNA LISTA DONDE GUARDAR LOS OBJETOS, LA CANTIDAD DE OBJETOS, EL ANCHO Y EL ALTO DEL MAPA.
    while len(list_objects) < num_objects:
        new_position = [randint(0,MAP_WIDTH),randint(0,MAP_HEIGHT)]
        
        if new_position not in list_objects and new_position != my_position:
            list_objects.append(new_position)

def map_with_walls():
    obstacle_definition= """\
        ############       ##
###     ####         ###    #
#####          ###   ####  ##
###### ###########   ####   #
        #########   ####   ##   
#######   ########         ##
#######   ###       #########
########   ##          ######
###                     ##### 
              #              
#####           ##  #########
###           #        ######
############             ####
###############     #   #####
##################          #
######################     ##\
"""
    return obstacle_definition


############################## | CONSTANTES | ##############################

POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 10


############################## | LISTAS | ##################################

my_position = [0,0]     # NUESTRA POSICIÓN
map_objects = []        # LISTA DE OBJETOS EN EL MAPA
tail = []               # LA COLA DE LA SERPIENTE


############################## | VARIABLES | ###############################

tail_lenght = 0         # EL LARGO DE LA COLA
points = 0              # CONTADOR DE PUNTOS
end_game = False        # FINALIZACION DEL JUEGO
die = False


############################# | OBSTACULOS EN EL MAPA | ###################

obstacles = map_with_walls()

obstacles = [list(row) for row in obstacles.split("\n")]      # PARTIMOS CADA LINEA DEL MAPA DE OBSTACULOS, EN UNA LISTA DE LISTAS.

MAP_WIDTH = len(obstacles[0])
MAP_HEIGHT = len(obstacles)

#################################################################################
############################## | P R O G R A M A | ##############################
#################################################################################

print("\n"*18)

while not end_game:

    random_objects_in_map(map_objects, NUM_OF_MAP_OBJECTS, MAP_WIDTH, MAP_HEIGHT)   #### VAMOS A GENERAR LOS OBJETOS DEL MAPA ALEATORIAMENTE.

    # CREAMOS EL MAPA
    print("\033[F" * 18 + "+" + "-" * MAP_WIDTH * 2 + "+")      # IMPRIMIMOS LA CABECERA DEL MAPA ||| CON EL COMANDO 033F TE VUELVE A LA LINEA ANTERIOR, AL MULTIPLICAR (*18) VUELVE AL PRINCIPIO Y TE VUELVE A PRINTEAR, ASÍ EVITAMOS EL PARPADEO Y BORRA LO QUE HAY EN LA PANTALLA.

    for coordinate_y in range(MAP_HEIGHT):      # IMPRIMIMOS EL ALTO DEL MAPA.
        print("|", end="")
        
        for coordinate_x in range(MAP_WIDTH):   # IMPRIMIMOS EL ANCHO DEL MAPA
            
            char_to_draw = "  "                  # CARACTER A PINTAR
            object_in_cell = None               # AQUÍ GUARDAREMOS QUE OBJETO HAY EN LA CELDA EN CADA MOMENTO PARA SOBREESCRIBIRLO
            tail_in_cell = None
            
            for map_object in map_objects:     # RECORREMOS LA LISTA DE OBJETOS EN EL MAPA

                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"          # EN CASO DE ENCONTRAR UN OBJETO PINTAMOS UN '*'
                    object_in_cell = map_object

            for tail_piece in tail:             # PINTAMOS TAMBIEN LOS OBJETOS DE LA COLA
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " #"
                    tail_in_cell = tail_piece

            
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:       # COMPROBAMOS SI LA POSICION X ES = A MI POSICION, PINTAMOS LA POSICION
                char_to_draw = " @"              # EN CASO DE ENCONTRAR NUESTRA POSICIÓN NOS PINTAMOS CON UNA '@'


                if object_in_cell:
                    map_objects.remove(object_in_cell)  # BORRAMOS EL OBJETO COMIDO DE LA LISTA DE OBJETOS
                    tail_lenght += 1        # SUMAMOS 1 A LA LONGITUD DE LA COLA
                    points += 10            # SUMAMOS LOS PUNTOS AL MARCADOR

                if tail_in_cell:    # SI EN LA CELDA QUE MOVEMOS LA CABEZA HAY UN TROZO DE LA COLA, MORIMOS
                    end_game = True
                    die = True

            if obstacles[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")      
    # IMPRIMIMOS EL CIERRE DEL MAPA

    direction = readchar.readchar().decode().lower()    
    #READCHAR nos va a devolver cualquier caracter que nosotros pulsemos como un string

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]


    elif direction == "u":
        end_game = True     # PONEMOS LETRA 'U' PARA PODER ROMPER EL BUCLE Y SALIR.


    if new_position:

        if obstacles[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())  # CON EL COPY CREAMOS UNA COPIA DE LA LISTA PARA QUE NO SE MODIFIQUE AL CAMBIAR LA ORIGINAL
            tail = tail[:tail_lenght]           # LE DAMOS LA LONGITUD MÁXIMA DE LA COLA
            my_position = new_position
        else:
            die = True

    #os.system("cls")    # LIMPIAMOS LA PANTALLA
    
if die == True:
    print("¡ HAS MUERTO !")
