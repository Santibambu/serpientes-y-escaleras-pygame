import pygame.mixer as mixer
import random

mixer.init()

def reproducir_música(estado_de_juego: str, duración: int = -1):
    """
    Reproduce la música correspondiente al estado del juego.

    Parámetros:
        estado_de_juego (str): El estado actual del juego.
        duración (int): Duración de la música en milisegundos. Por defecto es -1 (bucle).
    """
    músicas = {
        "inicio": "./musica/ancient_sadness.mp3",
        "nombre": "./musica/astrologer.mp3",
        "victoria": "./musica/grim.mp3",
        "derrota": "./musica/master_alarich_theme.mp3",
        "sin preguntas": "./musica/tavern_theme.mp3",
        "atrapado": "./musica/disturbing.mp3"
    }
    if not mixer.music.get_busy():
        for estado, canción in músicas.items():
            if estado == estado_de_juego:
                mixer.music.load(canción)
                mixer.music.play(duración)

def detener_música():
    """
    Detiene la música que se está reproduciendo.

    Parámetros:
        Ninguno
    """
    mixer.music.stop()

def reproducir_sonido(sonido: str):
    """
    Reproduce un efecto de sonido según el nombre indicado.

    Parámetros:
        sonido (str): Nombre del sonido a reproducir.
    """
    sonidos = {
        "click": "./sonidos/click.mp3",
        "escalera": "./sonidos/escalera.mp3",
        "serpiente": "./sonidos/serpiente.mp3",
        "temporizador": "./sonidos/temporizador.mp3"
    }
    for nombre_sonido, ruta_sonido in sonidos.items():
        if nombre_sonido == sonido:
            efecto = mixer.Sound(ruta_sonido)
            efecto.set_volume(0.4)
            efecto.play()

def reproducir_sonido_aleatorio():
    """
    Reproduce un sonido aleatorio de teclas.

    Parámetros:
        Ninguno
    """
    sonidos = ["./sonidos/tecla_1.mp3", "./sonidos/tecla_2.mp3", "./sonidos/tecla_3.mp3", "./sonidos/tecla_4.mp3"]
    número_aleatorio = random.randint(0, 3)
    sonido_aleatorio = sonidos[número_aleatorio]
    efecto = mixer.Sound(sonido_aleatorio)
    efecto.set_volume(0.4)
    efecto.play()