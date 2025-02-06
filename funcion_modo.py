import pygame
import json

pygame.init()
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)
VERDE_RECTANGULO = (56, 168, 56)
CELESTE_CIRC = (110, 192, 207)
AMARILLO = (255, 255, 0)
GRIS_MID = (150, 150, 150)
GRIS = (200, 200, 200)
GRIS_OSCURO = (50, 50, 50)
AZUL_TIEMPO = (70,130,180)
fuente = pygame.font.SysFont("consolas", 20)


def renderizar_img(facil: bool, normal: bool, dificil: bool, pokemon_adivinanza: dict):
    # Inicializa imagen_adivinanza con un valor predeterminado
    imagen_adivinanza = None

    # Si el modo normal está activo
    if normal:
        imagen_adivinanza = pygame.image.load(pokemon_adivinanza["imagen"])  # Carga la imagen del Pokémon
        imagen_adivinanza = pygame.transform.scale(imagen_adivinanza, (50, 50))  # Escala la imagen
    # Si el modo difícil está activo
    elif dificil:
        imagen_adivinanza = pygame.image.load(pokemon_adivinanza["imagen"])
        imagen_adivinanza = imagen_adivinanza.convert_alpha()  # Convierte la imagen para manejar la transparencia
        silueta_negra = pygame.Surface(imagen_adivinanza.get_size(), pygame.SRCALPHA)  # Crea una superficie para la silueta
        silueta_negra.fill((0, 0, 0, 0))  # Rellena con color transparente
        mascara = pygame.mask.from_surface(imagen_adivinanza)  # Crea una máscara de la imagen

        # Rellena la silueta con negro donde hay pixels de la imagen original
        for x in range(silueta_negra.get_width()):
            for y in range(silueta_negra.get_height()):
                if mascara.get_at((x, y)):
                    silueta_negra.set_at((x, y), NEGRO)

        silueta_negra.blit(imagen_adivinanza, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)  # Dibuja la imagen con la silueta
        imagen_adivinanza = silueta_negra
    else:  # Asumiendo que quieres manejar el caso 'facil' aquí
        imagen_adivinanza = pygame.image.load(pokemon_adivinanza["imagen"])  # Carga la imagen del Pokémon
        imagen_adivinanza = pygame.transform.scale(imagen_adivinanza, (250, 250))  # Escala la imagen

    return imagen_adivinanza  # Retorna la imagen renderizada


def seleccionar_modos(evento_pos, boton_facil, boton_normal, boton_dificil, modo_facil, modo_normal, modo_dificil):
    # Inicializa un nuevo estado para los modos
    nuevo_modo_facil = modo_facil
    nuevo_modo_normal = modo_normal
    nuevo_modo_dificil = modo_dificil

    # Verifica si el evento ocurrió sobre el botón fácil
    if boton_facil.collidepoint(evento_pos):
        nuevo_modo_facil = True
        nuevo_modo_normal = False
        nuevo_modo_dificil = False

    elif boton_normal.collidepoint(evento_pos):
        nuevo_modo_facil = False
        nuevo_modo_normal = True
        nuevo_modo_dificil = False

    elif boton_dificil.collidepoint(evento_pos):
        nuevo_modo_facil = False
        nuevo_modo_normal = False
        nuevo_modo_dificil = True

    return nuevo_modo_facil, nuevo_modo_normal, nuevo_modo_dificil


def dibujar_boton(ventana, estado, boton, texto):
    # Dibuja un botón en la ventana
    pygame.draw.rect(ventana, estado, boton, border_radius=10)  # Dibuja el rectángulo del botón
    texto_renderizado = fuente.render(str(texto), True, NEGRO)  # Renderiza el texto del botón
    ventana.blit(texto_renderizado, (boton.x + (boton.width - texto_renderizado.get_width()) // 2,
                                     boton.y + (boton.height - texto_renderizado.get_height()) // 2))  # Centra el texto


def dibujar_area_racha(ventana, color, rect, texto):
    # Dibuja un área en la ventana que muestra la racha actual
    pygame.draw.rect(ventana, color, rect, border_radius=10)  
    ventana.blit(texto, (rect.x + 5, rect.y + 5))  


# def dibujar_elemento_tiempo(ventana, color, rectangulo, texto):
#     # Dibuja un elemento en la ventana que muestra información de tiempo
#     pygame.draw.rect(ventana, color, rectangulo, border_radius=10)  # Dibuja el rectángulo del elemento
#     texto_superficie = fuente.render(str(texto), True, NEGRO)  # Renderiza el texto del elemento
#     ventana.blit(texto_superficie, (rectangulo.x + (rectangulo.width - texto_superficie.get_width()) // 2,
#                                     rectangulo.y + 5))  # Centra el texto


def guardar_pokemon_csv(pokemon):
    # Guarda la información de un Pokémon en un archivo CSV
    with open("pokemones_aparecidos.csv", "a", encoding="utf-8") as archivo:  
        linea = f"Nombre en inglés: {pokemon['nombre_ingles']}, Nombre en francés: {pokemon['nombre_frances']}, Nombre en italiano: {pokemon['nombre_italiano']}, Nombre en alemán: {pokemon['nombre_aleman']}\n"
        archivo.write(linea)  # Escribe la línea en el archivo


# Función lambda para actualizar la mejor racha y el texto correspondiente
# Ternario
mejor_streak_y_texto = lambda streak, best: (
    streak if streak > best else best,
    fuente.render("Mejor racha: " + str(streak if streak > best else best), True, NEGRO)
)  # Renderiza el texto de la mejor racha



# Función para guardar Pokémon en un archivo JSON
def guardar_pokemon_json(pokemon):
    # Cargar los datos existentes
    try:
        with open("pokemones_adivinados.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []  # Si el archivo no existe, inicializa una lista vacía
    datos.append(pokemon)

    # Guardar la lista actualizada en el archivo JSON
    with open("pokemones_adivinados.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)