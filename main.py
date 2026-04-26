import pygame

from config import *
from ui.button import Button
from core.array_utils import generate_array
from core.visualizer import BarAnimator
from algorithms.merge_sort import merge_sort

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

size_index = 1
array = generate_array(size_index)
animator = BarAnimator(array)

paused = True
step_mode = False
highlight = -1

generator = None
current_algorithm = "Merge"

# Botões cima
pause_btn = Button(20, 10, 100, 40, "Play", font)
reset_btn = Button(140, 10, 100, 40, "Reset", font)
size_btn = Button(260, 10, 140, 40, "Size", font)
mode_btn = Button(420, 10, 180, 40, "Mode: RealTime", font)
step_btn = Button(620, 10, 120, 40, "Step", font)

# Botões baixo
algorithms = ["Merge", "Bubble", "Selection"]
algo_buttons = []

for i, name in enumerate(algorithms):
    btn = Button(50 + i * 160, HEIGHT - 60, 140, 40, name, font)
    algo_buttons.append(btn)

def start_sort():
    global generator

    if current_algorithm == "Merge":
        generator = merge_sort(array, 0, len(array) - 1)

running = True
while running:
    clock.tick(60)
    screen.fill(BG_COLOR)

    # Cada evento é pego aqui, cliques e etc
    # Se for clicado em um botão executa uma ação
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pause_btn.clicked(event):
            paused = not paused
            if not generator:
                start_sort()

        if reset_btn.clicked(event):
            array = generate_array(size_index)
            animator = BarAnimator(array)
            generator = None
            highlight = -1

        if size_btn.clicked(event):
            size_index = (size_index + 1) % len(SIZES)
            array = generate_array(size_index)
            animator = BarAnimator(array)
            generator = None
            highlight = -1

        if mode_btn.clicked(event):
            step_mode = not step_mode

        if step_btn.clicked(event) and step_mode:
            paused = True
            if generator:
                try:
                    action = next(generator)

                    if action[0] == "overwrite":
                        _, i, val = action
                        array[i] = val
                        animator.overwrite(i, val)
                        highlight = i

                except StopIteration:
                    generator = None

        for btn in algo_buttons:
            if btn.clicked(event):
                current_algorithm = btn.text
                array = generate_array(size_index)
                animator = BarAnimator(array)
                generator = None
                highlight = -1

    if not paused and not step_mode and generator:
        try:
            action = next(generator)

            if action[0] == "swap":
                _, i, j = action
                array[i], array[j] = array[j], array[i]
                animator.swap(i, j)
                highlight = i

            elif action[0] == "overwrite":
                _, i, val = action
                array[i] = val
                animator.overwrite(i, val)
                highlight = i

        except StopIteration:
            generator = None

    animator.update()

    animator.draw(screen, highlight)

    pause_btn.text = "Play" if paused else "Pause"
    size_btn.text = f"Size: {SIZES[size_index]}"
    mode_btn.text = "Mode: Step" if step_mode else "Mode: RealTime"

    pause_btn.draw(screen)
    reset_btn.draw(screen)
    size_btn.draw(screen)
    mode_btn.draw(screen)
    step_btn.draw(screen)

    for btn in algo_buttons:
        btn.draw(screen, active=(btn.text == current_algorithm))

    pygame.display.update()

pygame.quit()