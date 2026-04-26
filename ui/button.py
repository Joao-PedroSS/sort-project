import pygame

class Button:
    def __init__(self, x, y, w, h, text, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font

    def draw(self, screen, active=False):
        mouse_pos = pygame.mouse.get_pos()
        
        # Cores
        base_color = (50, 35, 25)
        hover_color = (200, 110, 40)
        active_color = (255, 140, 0)

        if active:
            color = active_color
        elif self.rect.collidepoint(mouse_pos):
            color = hover_color
        else:
            color = base_color

        pygame.draw.rect(screen, color, self.rect)

        text_surface = self.font.render(self.text, True, (255, 245, 230))
        screen.blit(text_surface, text_surface.get_rect(center=self.rect.center))

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)