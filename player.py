import pygame

class Player:
    def __init__(self, x, y, image_path, size=(48,48)):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load(image_path), size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, keys, width, height):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < width - self.rect.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < height - self.rect.height:
            self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
