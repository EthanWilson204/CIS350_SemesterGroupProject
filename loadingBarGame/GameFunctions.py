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

def checkUpgrades(B1_rect, B2_rect, B3_rect, L1_speed, L2_speed, L3_speed, mouse):
    if B1_rect.collidepoint(mouse):
        print("button pressed")
        buttonUpgrades(L1_speed)
        print(L1_speed)
                
    if B2_rect.collidepoint(mouse):
        buttonUpgrades(L2_speed)
            
    if B3_rect.collidepoint(mouse):
        buttonUpgrades(L3_speed)
        