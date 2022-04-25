import pygame
from support import import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x,y):
        super().__init__()  # Herencia
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self, shift):
        self.rect.x += shift

class StaticTile(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        self.image = surface

# Crate is not 64x64 ¡¡¡
class Crate(StaticTile):
    def __init__(self, size,x,y):
        super().__init__(size,x,y,pygame.image.load('../graphics/terrain/crate.png').convert_alpha())

        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft = (x,offset_y)) # move crate

class AnimatedTile(Tile):
    def __init__(self,size,x,y,path):
        super().__init__(size,x,y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.10
        if self.frame_index >= len(self.frames): # number of frame images
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
        self.animate()
        self.rect.x += shift

class Coin(AnimatedTile):
    def __init__(self,size,x,y,path):
        super().__init__(size,x,y,path)
        offset_y = y + size // 2
        offset_x = x + size // 2
        self.rect = self.image.get_rect(center=(offset_x, offset_y))

class Palm(AnimatedTile):
    def __init__(self,size,x,y,path, offset):
        super().__init__(size,x,y,path)
        offset_y = y - offset
        self.rect = self.image.get_rect(topleft=(x,offset_y))
        #self.rect.topleft = (x, offset_y)