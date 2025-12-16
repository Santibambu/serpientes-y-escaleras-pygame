# Serpientes y Escaleras - Segundo Parcial de Programación I

Juego desarrollado en Python utilizando Pygame como proyecto académico para el segundo parcial de la materia Programación I en la UTN FRA.

## Descripción
Juego interactivo con mecánicas de tablero y preguntas, que utiliza una arquitectura basada en estados para controlar el flujo completo del juego, incluyendo inicio, ingreso de datos, juego activo, validación, resolución y finalización.

## Tecnologías
- Python  
- Pygame

## Estructura del proyecto
- `Juego.py`: archivo principal del programa  
- `Funciones/`: módulos que separan la lógica del juego (estados, archivos, validaciones, audio, etc.)  
- `Imágenes/`, `Sonidos/`, `Música/`: recursos multimedia utilizados  
- Archivos CSV para almacenamiento de datos y puntuaciones

## Ejecución
1. Clonar el repositorio  
2. Tener instalado Python 3.x  
3. Instalar Pygame:
   ```bash
   pip install pygame
5. Ejecutar:
   ```bash
   python Juego.py

## Objetivos del proyecto
- Aplicar una arquitectura modular y separación de responsabilidades  
- Implementar control de estados y flujo de juego  
- Gestionar eventos y temporización con Pygame  
- Persistir datos en archivos CSV y ordenarlos mediante funciones personalizadas  
- Integrar audio (música y efectos) de forma independiente
