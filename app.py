import pygame
from player import Player
from items import Item

WIDTH, HEIGHT = 600, 400
BG_COLOR = (255, 240, 245)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cafeteria Fofo")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = Player(WIDTH // 2, HEIGHT // 2, "images/gato.png")

item_images = [
    "images/bolo.png",
    "images/sanduiche.png",
    "images/refri.png",
    "images/sorvete.png",
    "images/biscoito.png",
    "images/pudim.png",
    "images/pudim_morango.png"
]

item = Item(WIDTH, HEIGHT, item_images, size=(64, 64))
score = 0
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH, HEIGHT)

    hitbox = player.rect.inflate(20, 20) 
    if hitbox.colliderect(item.rect):
        score += 1
        item.respawn()

    screen.fill(BG_COLOR)
    player.draw(screen)
    item.draw(screen)
    screen.blit(font.render(f"Score: {score}", True, (255, 105, 180)), (10, 10))

    pygame.display.flip()

pygame.quit()
