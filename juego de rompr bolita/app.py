import pygame
import sys

# Inicializar pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pelotita Rompe Paredes 🧱")

# --- Colores ---
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 150, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# --- Jugador (paleta) ---
paleta = pygame.Rect(ANCHO//2 - 60, ALTO - 40, 120, 15)
vel_paleta = 7

# --- Pelota ---
pelota = pygame.Rect(ANCHO//2 - 10, ALTO//2 - 10, 20, 20)
vel_pelota = [5, -5]

# --- Bloques ---
bloques = []
for fila in range(5):
    for col in range(8):
        bloque = pygame.Rect(100 * col + 35, 50 * fila + 30, 80, 25)
        bloques.append(bloque)

# --- Bucle principal ---
reloj = pygame.time.Clock()
running = True

while running:
    reloj.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Movimiento de la paleta ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and paleta.left > 0:
        paleta.x -= vel_paleta
    if teclas[pygame.K_RIGHT] and paleta.right < ANCHO:
        paleta.x += vel_paleta

    # --- Movimiento de la pelota ---
    pelota.x += vel_pelota[0]
    pelota.y += vel_pelota[1]

    # Rebote contra las paredes
    if pelota.left <= 0 or pelota.right >= ANCHO:
        vel_pelota[0] = -vel_pelota[0]
    if pelota.top <= 0:
        vel_pelota[1] = -vel_pelota[1]

    # Si cae abajo → perder
    if pelota.bottom >= ALTO:
        print("💀 Game Over 💀")
        running = False

    # Rebote con la paleta
    if pelota.colliderect(paleta):
        vel_pelota[1] = -vel_pelota[1]

    # Colisión con bloques
    for bloque in bloques[:]:
        if pelota.colliderect(bloque):
            bloques.remove(bloque)
            vel_pelota[1] = -vel_pelota[1]
            break

    # --- Dibujar todo ---
    VENTANA.fill(NEGRO)
    pygame.draw.rect(VENTANA, AZUL, paleta)
    pygame.draw.ellipse(VENTANA, BLANCO, pelota)

    for bloque in bloques:
        pygame.draw.rect(VENTANA, VERDE, bloque)

    pygame.display.flip()

pygame.quit()
sys.exit()
