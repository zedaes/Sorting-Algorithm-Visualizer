import pygame as pg
import sys
import time
from constants import *
from sorting_algorithms import SortingAlgorithms

class Engine:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((window_width, window_height))
        pg.display.set_caption("Sorting Algorithm Visualizer")
        self.clock = pg.time.Clock()
        self.sorting_algorithms = SortingAlgorithms(window=self.window)
        self.sorting_start_time = None
        self.sorting_end_time = None

        self.algorithms = {
            pg.K_1: self.sorting_algorithms.bubble_sort,
            pg.K_2: self.sorting_algorithms.selection_sort,
            pg.K_3: self.sorting_algorithms.insertion_sort,
            pg.K_4: self.sorting_algorithms.quick_sort,
            pg.K_5: self.sorting_algorithms.partition
        }

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    self.reset_sort()
                elif event.key in self.algorithms:
                    self.start_sorting(event.key)

    def start_sorting(self, key):
        self.sorting_algorithms.sorting_generator = self.algorithms[key]()
        self.sorting_start_time = time.time()  # Start the timer when sorting begins

    def reset_sort(self):
        self.sorting_algorithms.reset()
        self.sorting_start_time = None
        self.sorting_end_time = None

    def draw(self):
        self.window.fill(white)
        # Ensure bars fit within the window height
        max_value = max(self.sorting_algorithms.values)
        scaling_factor = (window_height - 10) / max_value  # Leave some margin for aesthetics
        
        for i, value in enumerate(self.sorting_algorithms.values):
            # Old color scheme based on height
            color = (255 - int(value * 255 / max_value), int(value * 255 / max_value), 0)  # Green to red gradient
            pg.draw.rect(
                self.window,
                color,
                (i * square_size, window_height - value * scaling_factor, square_size, value * scaling_factor)
            )
        pg.display.update()


    def run(self):
        while True:
            self.events()
            if self.sorting_algorithms.sorting_generator:
                try:
                    next(self.sorting_algorithms.sorting_generator)
                except StopIteration:
                    self.sorting_algorithms.sorting_generator = None
                    self.sorting_end_time = time.time()  # Record end time
                    self.display_sorting_time()  # Display and reset the bars
            self.draw()


    def display_sorting_time(self):
        if self.sorting_start_time and self.sorting_end_time:
            sort_time = self.sorting_end_time - self.sorting_start_time
            print(f"Sorting completed in {sort_time:.2f} seconds.")
            self.reset_sort()  # Shuffle values for another round of sorting

if __name__ == '__main__':
    engine = Engine()
    engine.run()
