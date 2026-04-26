import random
from config import HEIGHT, TOP_HEIGHT, BOTTOM_HEIGHT, SIZES

def generate_array(size_index):
    size = SIZES[size_index]
    max_height = HEIGHT - TOP_HEIGHT - BOTTOM_HEIGHT - 20
    return [random.randint(10, max_height) for _ in range(size)]