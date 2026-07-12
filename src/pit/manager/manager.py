import pygame

class ScreenManager():
    def __init__(self, screen : pygame.Surface):
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def update(self):
        surf = pygame.surface.Surface((200,100))
        surf.fill((0,0,0))
        rect = pygame.rect.Rect(self.width//2-100, self.height//2-50, 200, 100)
        self.screen.blit(surf, rect)