import pygame
from pygame.locals import *
from pygame.gfxdraw import *

CIRCLE_RADIUS = 3
GREEN = (0, 255, 0)


class GUI:
    def __init__(self, width, height, data_transfer, listener):
        self._running = True
        self._display_surface = None
        self.size = width, height
        self._data_transfer = data_transfer
        self._listener = listener

    def on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self._listener:
                self._listener.on_down()

    def on_loop(self):
        config = self._data_transfer.get_next_configuration()
        if config:
            self._display_surface.fill((0,0,0))
            for point in config:
                pygame.gfxdraw.circle(self._display_surface, point[0], point[1], CIRCLE_RADIUS, GREEN)
            pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()
        clock = pygame.time.Clock()
        while self._running:
            clock.tick(50)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
        self.on_cleanup()
