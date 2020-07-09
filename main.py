import pygame
import player as Player
import grid as Grid
import constants
import log as Log

def main():
    # Basics variables and instantiations
    WHITE = (255, 255, 255)
    clock = pygame.time.Clock()
    running = True
    pygame.init()
    WIDTH, HEIGHT = 820, 710
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    # Basics classes intantiations - TODO: Work with multiple screens and change this up
    player = Player.Player('Player', 340, [34, 34], 40, 100, win, size=[10, 10])
    enemy = Player.Player('Enemy', 340, [34, 34], 420, 100, win, size=[10, 10])
    ships_grid = Grid.Grid([470, 190], 40, 490, constants.BLACK, win, size=[0, 0])
    logs_grid = Grid.Grid([250, 190], 530, 490, constants.BLACK, win, size=[0,0])

    log = Log.Log(win, 520, 500)

    while running:
        clock.tick(60)
        win.fill(WHITE)

        # Drawing basics objects - TODO: Change this up when using multiple screens+events
        player.draw_grid()
        player.draw_title_message("My Ships")
        enemy.draw_grid()
        enemy.draw_title_message("Enemy Ships")

        ships_grid.draw_ships_list()
        logs_grid.draw_ships_list()

        log.draw_log()

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                print('Clicked at ', pos)
                player.collide_check(pos)
                enemy.collide_check(pos)

        pygame.display.update()

main()