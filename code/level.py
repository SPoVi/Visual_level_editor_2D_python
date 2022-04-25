import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tile import Tile, StaticTile, Crate, Coin, Palm

class Level:
    def __init__(self, level_data, surface):
        # general setup
        self.display_surface = surface
        self.world_shift = 0

        # terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        # grass setup
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')

        # grass setup
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')

        # crates
        crates_layout = import_csv_layout(level_data['crates'])
        self.crates_sprites = self.create_tile_group(crates_layout, 'crates')

        # coins
        coins_layout = import_csv_layout(level_data['coins'])
        self.coins_sprites = self.create_tile_group(coins_layout,'coins')

        # foreground palms
        fg_palms_layout = import_csv_layout(level_data['fg palms'])
        self.fg_palms_sprites = self.create_tile_group(fg_palms_layout, 'fg palms')

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('../graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(val)] # get the right tile
                        sprite = StaticTile(tile_size,x,y,tile_surface)


                    if type == 'grass':
                        grass_tile_list = import_cut_graphics('../graphics/decoration/grass/grass.png')
                        tile_surface = grass_tile_list[int(val)] # get the right tile
                        sprite = StaticTile(tile_size,x,y,tile_surface)

                    if type == 'crates':
                        sprite = Crate(tile_size,x,y)

                    if type == 'coins':
                        if val == '0': # gold
                            sprite = Coin(tile_size,x,y,'../graphics/coins/gold')
                        elif val == '1': # silver
                            sprite = Coin(tile_size,x,y,'../graphics/coins/silver')

                    if type == 'fg palms':
                        if val == '0':
                            sprite = Palm(tile_size,x,y,'../graphics/terrain/palm_small',38)
                        if val == '1':
                            sprite = Palm(tile_size,x,y,'../graphics/terrain/palm_large',69)



                    sprite_group.add(sprite)

        return sprite_group

    def run(self):

        # run the entire game/level
        # terrain
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        # grass
        self.grass_sprites.update(self.world_shift)
        self.grass_sprites.draw(self.display_surface)

        #crate
        self.crates_sprites.update(self.world_shift)
        self.crates_sprites.draw(self.display_surface)

        # coins
        self.coins_sprites.update(self.world_shift)
        self.coins_sprites.draw(self.display_surface)

        # plams
        self.fg_palms_sprites.update(self.world_shift)
        self.fg_palms_sprites.draw(self.display_surface)
