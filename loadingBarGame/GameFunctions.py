import pygame
#add money to the total
def addMoney(user_money, bar_amt):
    user_money += bar_amt

#upgrade buttons to make them faster
def buttonUpgrades(bar_speed):
    
    bar_speed *= 1.5
    #upgrade counter -= 1

#display the text on different buttons
def TextDisplay(screen, text, text_font, text_x, text_y):
     text_img = pygame.font.Font.render(text_font, text, True, ('white'))
     screen.blit(text_img, (text_x,text_y))

    