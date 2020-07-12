import pygame
import player as Player
import grid as Grid
import constants
import log as Log
import ship as Ship
import random

def main():
    # List of Ships - TODO: Move it to somewhere else later
    ships_list = [
        {'image': 'images/carrier.png', 'name': 'Carrier', 'size': 5, 'x':90, 'y':490, 'pg_image': pygame.image.load('images/carrier.png')},
        {'image': 'images/battleship.png', 'name': 'Battleship', 'size': 4, 'x':150, 'y':490, 'pg_image': pygame.image.load('images/battleship.png')},
        {'image': 'images/cruiser.png', 'name': 'Cruiser', 'size': 3, 'x':210, 'y':490, 'pg_image': pygame.image.load('images/cruiser.png')},
        {'image': 'images/submarine.png', 'name': 'Submarine', 'size': 3, 'x':270, 'y':490, 'pg_image': pygame.image.load('images/submarine.png')},
        {'image': 'images/destroyer.png', 'name': 'Destroyer', 'size': 2, 'x':330, 'y':490, 'pg_image': pygame.image.load('images/destroyer.png')},
    ]

    #ships_list_images = [pygame.image.load(i['image']) for i in ships_list]

    # Basics variables and instantiations
    WHITE = (255, 255, 255)
    clock = pygame.time.Clock()
    running = True
    pygame.init()
    WIDTH, HEIGHT = 820, 690
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    win.fill(WHITE)

    # Basics classes intantiations - TODO: Work with multiple screens and change this up
    player = Player.Player('Player', 340, [34, 34], 60, 120, win, size=[10, 10])
    enemy = Player.Player('Enemy', 340, [34, 34], 440, 120, win, size=[10, 10])
    ships_grid = Grid.Grid([380, 190], 60, 480, constants.BLACK, win, size=[0, 0])
    logs_grid = Grid.Grid([300, 190], 468, 480, constants.BLACK, win, size=[0, 0])
    # log = Log.Log(win, 520, 500) # For Testing

    # Drawing list of ships
    my_ships = []
    for index, item in enumerate(ships_list):
        ship = Ship.Ship(item['pg_image'], item['name'], item['x'], item['y'], item['size'], win)
        my_ships.append(ship)
        ship.draw_ships_list()
    
    def redraw():
        win.fill(WHITE)

        # Drawing basics objects - TODO: Change this up when using multiple screens+events
        player.draw_grid()
        enemy.draw_grid()

        # Drawing grid with list of ships and log menu
        ships_grid.draw_ships_list()
        logs_grid.draw_ships_list()
        # log.draw_log() # For Testing

        for ship in my_ships:
            ship.draw_image(ship.x, ship.y)

        pygame.display.flip()

    # List of ships inside player grid
    ships_in_grid = []

    while running:

        p_check_rect = []

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Get mouse position
                    pos = pygame.mouse.get_pos()
                    print('Clicked at ', pos)
                    
                    # Check collision with player and enemy grid grid - TODO: Improve logic
                    # p_collided = player.collide_check(pos)
                    # enemy.collide_check(pos)

                    # Testing drawing boat on grid
                    #if p_collided:
                        #my_ships[random.randrange(5)].draw_image(p_collided[0][0], p_collided[0][1])
                    
                    for ship in my_ships:
                        if ship.rect.collidepoint(pos):
                            ship.drag = True
                            break
            
            if event.type == pygame.MOUSEBUTTONUP:
                # Check if player can drop ship at pos - If no return ship to initial position
                
                for ship in my_ships:

                    if ship.drag:
                        left_check_rect = player.collide_check((ship.x + ship.rect[2] / 2, ship.y))
                        if len(left_check_rect) > 0:
                            print('left_check_rect', left_check_rect)
                            new_ship_x_y = player.check_ship_in_bounds(left_check_rect, ship)
                            ship.x, ship.y = new_ship_x_y
                        else:
                            right_check_rect = player.collide_check((ship.x + 20, ship.y))
                            
                            if len(right_check_rect) > 0:
                                pass
                                #print('right_check_rect')
                        #if ship not in ships_in_grid:
                        #    ships_in_grid.append(ship)

                        ship.drag = False
        
        for ship in my_ships:
            if ship.drag:

                pos = pygame.mouse.get_pos()
                ship.x = pos[0] - (ship.rect[2] / 2)
                ship.y = pos[1] - (ship.rect[3] / 2)

                ship.draw_image(ship.x, ship.y)
                break
        
        redraw()
        clock.tick(60)

main()