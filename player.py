import pygame
import grid as Grid
import constants
import log as Log
import ship as Ship


class Player:

    pygame.font.init()
    title_font = pygame.font.Font("fonts/Vollkorn-Bold.ttf", 40)

    def __init__(self, alias, canvas, blockSize, x, y, win, **kwargs):
        self.alias = alias
        self.size = kwargs.get('size', None)
        self.canvas = canvas
        self.blockSize = blockSize
        self.x = x
        self.y = y
        self.grid = []
        self.win = win
        self.color = (0, 0, 0)
        self.g_ = None
        self.grid = Grid.Grid(self.blockSize, self.x, self.y, self.color, self.win, size=self.size, alias=self.alias) 
    
    def draw_grid(self):
        self.g_ = self.grid.draw()
        self.draw_title_message()

        # Drawing axis labels (a-z 1-10)
        self.draw_grid_labels()

    def draw_grid_labels(self):
        self.grid.draw_grid_labels(self.g_)

    def draw_title_message(self):
        if self.alias == 'Player':
            text = self.title_font.render("My Ships", True, constants.PLAYER_TITLE_COLOR)
            self.win.blit(text, (self.x + 75, self.y - 90))
        else:
            text = self.title_font.render("Enemy Ships", True, constants.PLAYER_TITLE_COLOR)
            self.win.blit(text, (self.x + 45, self.y - 90))

    def collide_check(self, pos):
        '''
        Check for collision on the grid (Player or Enemy)

        Args:
            pos (touple): Coordinates clicked by users mouse (x,y)

        Returns:
            The coordinates of the grid
        '''
        for rect in self.g_:
            if rect[0].collidepoint(pos):
                collide_to = 'Collide to ' + str(self.alias) + ' on '+ str(pos)
                position = str(rect[1][0]) + ', ' + str(rect[1][1])
                print(collide_to + ' at x, y = ' + position)

                print('Rect ', rect[0])

                #log = Log.Log(self.win, 550, 510)
                #log.show_message(self.win, attacker='Player', defender='Enemy', type='HIT', position=position)

                return [rect[0], pos, (rect[1][0], rect[1][1])]

                break 
        
        return []

    def collide_check_rect(self, rect, list_recs):
        collided = False
        for item in list_recs:
            if item.rect != rect:
                if item.rect.colliderect(rect):
                    collided = True
                    break
        return collided

    def check_ship_in_bounds(self, rect, ship):
        x, y = ship.x, ship.y

        print('rect', rect[1][1])

        ship_center = ship.x + ship.rect[2] / 2
        grid_center = rect[0].left + 34 / 2

        if ship_center > grid_center:
            x = rect[0].left
        else:
            x = rect[0].left

        # Check if the grid can fit the ship height
        grid_y_pos = rect[2][0]
        y = ship.check_y_boundary(grid_y_pos, rect[0].top)
        return x, y