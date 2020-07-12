import pygame

class Ship(pygame.sprite.Sprite):
    
    def __init__(self, image, name, x, y, size, win):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.scale_image(image, size)
        self.name = name
        self.rect = None
        self.init_x = x
        self.init_y = y
        self.x = x
        self.y = y
        self.size = size
        self.win = win
        self.drag = False

    def draw_ships_list(self):
        self.rect = self.win.blit(self.image, (self.x, self.y))

    def scale_image(self, image, size):
        transform = pygame.transform.scale(image, (30, size * 30))
        return transform

    def draw_image(self, x, y):
        self.rect = self.win.blit(self.image, (x + 1, y + 2))

    def check_y_boundary(self, grid_y_pos, grid_top):
        print('checking ' + str(grid_y_pos) + ' at top ' + str(grid_top) + ' w/ boat size ' + str(self.size))
        if self.size in (2, 3, 4, 5) and grid_y_pos == 9:
            if self.size in (4, 5):
                return (grid_top - ((self.size - 1) * 34)) + 4 # extra spacing
            return grid_top - ((self.size - 1) * 34)
        
        if self.size in (2, 3, 4, 5) and grid_y_pos == 0:
            if self.size in (4, 5):
                return grid_top + 4 # extra spacing
            return grid_top

        if self.size == 2 and grid_y_pos < 9:
            return grid_top
        
        print(self.size)
        print(grid_y_pos)
        if self.size == 3 and grid_y_pos in range(0, 8):
            return grid_top
        if self.size == 3 and grid_y_pos == 8:
            return grid_top - 34
        
        if self.size == 4 and grid_y_pos in range(0, 7):
            return grid_top + 4 # extra spacing
        if self.size == 4 and grid_y_pos == 8:
            return (grid_top - (34 * 2)) + 4 # extra spacing
        if self.size == 4 and grid_y_pos == 7:
            return (grid_top - 34) + 4 # extra spacing
        
        if self.size == 5 and grid_y_pos in range(0, 6):
            return grid_top
        if self.size == 5 and grid_y_pos == 8:
            return grid_top - (34 * 3)
        if self.size == 5 and grid_y_pos == 7:
            return grid_top - (34 * 2)
        if self.size == 5 and grid_y_pos == 6:
            return grid_top - (34)

        print('got here ?')
        return grid_top
