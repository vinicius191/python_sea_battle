import pygame
import constants

class Log:
    
    pygame.font.init()
    log_font = pygame.font.Font("fonts/Vollkorn-Bold.ttf", 18)
    log_list = []

    def __init__(self, win, xStart, yStart, *args, **kwargs):
        self.win = win
        self.xStart = xStart
        self.yStart = yStart
        self.attacker = kwargs.get('attacker', None)
        self.defender = kwargs.get('defender', None)
        self.position = kwargs.get('position', None)
        self.type_ = kwargs.get('type', None)
        self.full_message = kwargs.get('full_message', None)
        
    def show_message(self, win, **kwargs):
        attacker = kwargs.get('attacker', None)
        defender = kwargs.get('defender', None)
        position = kwargs.get('position', None)
        type_ = kwargs.get('type', None)
        full_message = kwargs.get('full_message', None)
        
        text = ''

        if attacker:
            text = attacker + ' ' + type_ + ' ' + defender + ' at ' + position
        else:
            text = full_message
        
        log = self.log_font.render(text, True, constants.LOG_TEXT_COLOR)
        if len(self.log_list) > 7:
            self.log_list.clear()
        
        self.log_list.append(log)
    
    def draw_log(self):
        print('log list', len(self.log_list))
        for log in reversed(self.log_list):
            self.win.blit(log, (self.xStart + 20, self.yStart + (self.log_list.index(log) * 20)))
            
