import pygame
import random

class Item:
    def __init__(self, width, height, image_paths, size=(64, 64)):
        self.width = width
        self.height = height
        self.size = size
        self.images = [pygame.transform.scale(pygame.image.load(path), size) for path in image_paths]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        max_x = max(10, self.width - self.rect.width - 10)
        max_y = max(10, self.height - self.rect.height - 10)
        self.x = random.randint(10, max_x)
        self.y = random.randint(10, max_y)
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
