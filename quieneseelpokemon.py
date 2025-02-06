import random
import pygame
from funcion_modo import *
from generaciones import *
lista_pokemones = []
pygame.init()

ventana = pygame.display.set_mode((800, 800))
fondo_menu = pygame.image.load("Joaco-programacion/imagenes/fondomenu.jpg").convert()
fuente = pygame.font.SysFont("consolas", 20)
color_inactivo_text = GRIS_MID
color_activo_text = BLANCO
color_pordefecto = color_inactivo_text
activo_text= False
input_box = pygame.Rect(300, 575, 160, 35)
boton_jugar = pygame.Rect(290, 400, 200, 50)

pygame.mixer.music.load("Joaco-programacion/musica_fondo.mp3")
pygame.mixer.music.set_volume(0.1)

################# GENERECIONES #################
color_activo = GRIS_OSCURO
color_inactivo = GRIS_MID

boton_gen_1 = pygame.Rect(2, 150, 130, 35)
estado_gen_1 = color_activo
gen_1 = True
boton_gen_2 = pygame.Rect(2, 200, 130, 35)
estado_gen_2 = color_inactivo
gen_2 = False
boton_gen_3 = pygame.Rect(2, 250, 130, 35)
estado_gen_3 = color_inactivo
gen_3 = False

################# DIFICULTADES #################
boton_facil = pygame.Rect (640, 150, 130, 35) 
estado_facil = color_inactivo
modo_facil = False
boton_normal = pygame.Rect (640, 200, 130, 35) 
estado_normal = color_activo
modo_normal = True
boton_dificil = pygame.Rect (640, 250, 130, 35)
estado_dificil = color_inactivo
modo_dificil = False

################# TIEMPO #################
# tiempo = pygame.Rect((630, 150, 130, 85))
# tiempo_ant = pygame.Rect((630, 300, 130, 85))
# promedio = pygame.Rect((630, 450, 130, 85))
# tiempo_rect = pygame.Rect((630, 150, 130, 85))

################# RACHA #################
texto_racha = fuente.render("Racha: ", True, NEGRO)
texto_racha_max = fuente.render("Mejor racha: ", True, NEGRO)

racha = pygame.Rect(175, 620, 100, 35)
racha_max = pygame.Rect(350, 620, 180, 35)

contador_best = 0
bandera_ejecucion = True
while bandera_ejecucion:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera_ejecucion = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:

            if boton_jugar.collidepoint(evento.pos):
                pygame.mixer.music.play(-1)
                primera_vuelta = True
                ventana.fill(ROJO)
                icono = pygame.image.load("imagenes/cualesdeverdad.png")
                pygame.display.set_icon(icono)
                ################## DIBUJAR POKEDEX ####################
                pygame.draw.rect(ventana, BLANCO, (110, 110, 550, 550))
                pygame.draw.line(ventana, AZUL_CLARO, (260,670), (200, 670), 10)
                pygame.draw.line(ventana, VERDE, (300,670), (360, 670), 10)
                pygame.draw.circle(ventana, NEGRO, (150, 715), 33, 23)
                pygame.draw.rect(ventana, VERDE_RECTANGULO, (210, 700, 150, 70))
                pygame.draw.circle(ventana, CELESTE_CIRC, (33, 35), 28, 28)
                pygame.draw.circle(ventana, VERDE, (115, 35), 8, 8)
                pygame.draw.circle(ventana, AMARILLO, (90, 35), 8, 8)
                cruz = pygame.image.load("imagenes/cruz.png")
                cruz = pygame.transform.scale(cruz, (75, 75))
                ventana.blit(cruz, (550, 675))
                imagen_principal = pygame.image.load("imagenes/cualesdeverdad.png")
                imagen_principal = pygame.transform.scale(imagen_principal, (200, 120))
                ventana.blit(imagen_principal, (274, 3))
                fondo_pokedex = pygame.image.load("imagenes/campobatalla.png")
                fondo_pokedex = pygame.transform.scale(fondo_pokedex, (470, 465))
                ventana.blit(fondo_pokedex, (150, 150))
                pygame.draw.line(ventana, NEGRO, (550,630), (630, 630), 5)
                pygame.draw.line(ventana, NEGRO, (550,640), (630, 640), 5)
                pygame.draw.line(ventana, NEGRO, (550,650), (630, 650), 5)
                pygame.draw.circle(ventana, ROJO, (150, 643), 13, 13)
                pygame.draw.circle(ventana, ROJO, (350, 121), 5, 5)
                pygame.draw.circle(ventana, ROJO, (400, 121), 5, 5)
                texto = ""

                contador_streak = 0
                juego_activo = True
                while juego_activo:
                    if gen_1:
                        estado_gen_1 = color_activo
                        for i in range(len(pokemones_gen_1)):
                            lista_pokemones.append(pokemones_gen_1[i])
                    else:
                        estado_gen_1 = color_inactivo

                    if gen_2:
                        estado_gen_2 = color_activo
                        for i in range(len(pokemones_gen_2)):
                            lista_pokemones.append(pokemones_gen_2[i])
                    else:
                        estado_gen_2 = color_inactivo

                    if gen_3:
                        estado_gen_3 = color_activo
                        for i in range(len(pokemones_gen_3)):
                            lista_pokemones.append(pokemones_gen_3[i])
                    else:
                        estado_gen_3 = color_inactivo

                    if activo_text:
                        color_pordefecto = color_activo_text
                    else:
                        color_pordefecto = color_inactivo_text

                    if primera_vuelta:
                        pokemon_elegido = random.choice(lista_pokemones)
                        imagen_a_mostrar = renderizar_img(modo_facil, modo_normal, modo_dificil, pokemon_elegido)
                        imagen_a_mostrar = pygame.transform.scale(imagen_a_mostrar, (200,200))
                        ventana.blit(imagen_a_mostrar, (275, 300))
                        print(pokemon_elegido)
                        primera_vuelta = False
                        
                    pygame.display.update()
                    
                    for evento in pygame.event.get():
                        
                        if evento.type == pygame.QUIT:
                                juego_activo = False
                        elif evento.type == pygame.MOUSEBUTTONDOWN:
                            if boton_gen_1.collidepoint(evento.pos):
                                    if gen_1 == True and gen_2 == False and gen_3 == False:
                                        pass
                                    else:
                                        gen_1 = not gen_1
                            if boton_gen_2.collidepoint(evento.pos):
                                    if gen_1 == False and gen_2 == True and gen_3 == False:
                                        pass
                                    else:
                                        gen_2 = not gen_2
                            if boton_gen_3.collidepoint(evento.pos):
                                    if gen_1 == False and gen_2 == False and gen_3 == True:
                                        pass
                                    else:
                                        gen_3 = not gen_3    
                            if input_box.collidepoint(evento.pos):
                                activo_text = not activo_text 
                            ################# BOTONES  (MODOS) #################
                            modo_facil, modo_normal, modo_dificil = seleccionar_modos(evento.pos, boton_facil, boton_normal, boton_dificil, modo_facil, modo_normal, modo_dificil)
                        
                        elif evento.type == pygame.KEYDOWN:
                            if activo_text:
                                if evento.key == pygame.K_BACKSPACE:
                                    texto = texto[:-1]
                                else:
                                    #Renderiza el texto actual para obtener su ancho
                                    texto_superficie = fuente.render(texto + evento.unicode, True, NEGRO)
                                    #Agrega el nuevo carácter si no excede el ancho del rectángulo
                                    if texto_superficie.get_width() <= input_box.width - 10:  
                                        texto += evento.unicode
                            if evento.key == pygame.K_RETURN:
                                texto = texto.strip("\r") #pikachu\r, el unicode del enter
                                if texto.lower() == pokemon_elegido["nombre_ingles"].lower() or texto.lower() == pokemon_elegido["nombre_frances"].lower() or texto.lower() == pokemon_elegido["nombre_italiano"].lower() or texto.lower() == pokemon_elegido["nombre_aleman"].lower(): 
                                    guardar_pokemon_csv(pokemon_elegido)
                                    guardar_pokemon_json(pokemon_elegido)
                                    contador_streak += 1
                                    if contador_streak == 10:
                                        texto_racha = fuente.render("Racha: ", True, NEGRO)
                                        ventana.blit(texto_racha, (175, 620))
                                        contador_streak = 0
                                        pygame.time.delay(1000)
                                        juego_activo = False
                                        
                                    if contador_streak > contador_best:
                                        contador_best, texto_racha_max = mejor_streak_y_texto(contador_streak, contador_best)
                                    texto_racha = fuente.render("Racha: " + str(contador_streak), True, NEGRO)
                                    pokemon_elegido = random.choice(lista_pokemones)
                                    texto = ""
                                    imagen_a_mostrar = renderizar_img(modo_facil, modo_normal, modo_dificil, pokemon_elegido)
                                    imagen_a_mostrar = pygame.transform.scale(imagen_a_mostrar, (200,200))
                                    ventana.blit(fondo_pokedex, (150, 150))
                                    ventana.blit(imagen_a_mostrar, (275, 300))
                                    lista_pokemones = []
                                else:
                                    guardar_pokemon_csv(pokemon_elegido)
                                    juego_activo = False
                                    texto_racha = fuente.render("Racha: ", True, NEGRO)
                                    lista_pokemones = []

                    ################# GENERECIONES #################
                    dibujar_boton(ventana, estado_gen_1, boton_gen_1, "GEN 1")
                    dibujar_boton(ventana, estado_gen_2, boton_gen_2, "GEN 2")
                    dibujar_boton(ventana, estado_gen_3, boton_gen_3, "GEN 3")
                    
                    ################# DIFICULTADES #################
                    dibujar_boton(ventana, estado_facil, boton_facil, "FACIL")
                    dibujar_boton(ventana, estado_normal, boton_normal, "NORMAL")
                    dibujar_boton(ventana, estado_dificil, boton_dificil, "DIFICL")
                    
                    ################# TIEMPO #################
                    # dibujar_elemento_tiempo(ventana, AZUL_TIEMPO, tiempo, "TIEMPO:\n")
                    # dibujar_elemento_tiempo(ventana, AZUL_TIEMPO, tiempo_ant, "TIEMPO ANT")
                    # dibujar_elemento_tiempo(ventana, AZUL_TIEMPO, promedio, "PROMEDIO")
                    
                    ################# RACHA #################
                    dibujar_area_racha(ventana, GRIS, racha, texto_racha)
                    dibujar_area_racha(ventana, GRIS, racha_max, texto_racha_max)

                    ################# TEXT_BOX #################
                    pygame.draw.rect(ventana, color_pordefecto, input_box,border_radius = 10)
                    pygame.draw.rect(ventana, color_pordefecto, input_box, 5, border_radius = 10)
                    texto_superficie = fuente.render(texto, True, NEGRO)
                    ventana.blit(texto_superficie, (input_box.x + 5, input_box.y + 7))

                    if modo_facil:
                        estado_facil = color_activo
                    else:
                        estado_facil = color_inactivo
                    
                    if modo_normal:
                        estado_normal = color_activo
                    else:
                        estado_normal = color_inactivo
                    
                    if modo_dificil:
                        estado_dificil = color_activo
                    else:
                        estado_dificil = color_inactivo
    ventana.blit(fondo_menu, [0, 0])
    dibujar_boton(ventana, AMARILLO, boton_jugar, "JUGAR")

    pygame.display.update()
pygame.quit()