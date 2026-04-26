import pygame
from config import *

class Bar:
    def __init__(self, value, index, width):
        self.value = value
        self.width = width

        self.x = index * width
        self.target_x = self.x

    def update(self):
        speed = 10

        if self.x < self.target_x:
            self.x += min(speed, self.target_x - self.x)
        elif self.x > self.target_x:
            self.x -= min(speed, self.x - self.target_x)


class BarAnimator:
    def __init__(self, arr):
        self.bar_width = WIDTH // len(arr)
        self.bars = [Bar(v, i, self.bar_width) for i, v in enumerate(arr)]

    def update(self):
        for bar in self.bars:
            bar.update()

    def swap(self, i, j):
        # troca lógica
        self.bars[i], self.bars[j] = self.bars[j], self.bars[i]

        # define novos destinos
        self.bars[i].target_x = i * self.bar_width
        self.bars[j].target_x = j * self.bar_width

    def overwrite(self, i, value):
        self.bars[i].value = value

    def draw(self, screen, highlight):
        area_height = HEIGHT - TOP_HEIGHT - BOTTOM_HEIGHT

        for i, bar in enumerate(self.bars):
            color = HIGHLIGHT_COLOR if i == highlight else BAR_COLOR

            rect = (
                int(bar.x),
                TOP_HEIGHT + (area_height - bar.value),
                bar.width - 2,
                bar.value
            )

            pygame.draw.rect(screen, color, rect, border_radius=3)