import pygame
import random

#add money to the total
def addMoney(user_money, bar_amt):
    user_money += bar_amt

#upgrade buttons to make them faster
def buttonUpgrades(bar, bar_speed):
    #if the bar is not currently purchased the speed will be 0
    if bar_speed == 0:
        #if a zero speed bar is upgraded set it's base speed based on which bar it is
        if bar == 'L2':
            bar_speed += 1.5
        if bar == 'L3':
            bar_speed += 0.75
    else:
        bar_speed *= 1.5
    #upgrade counter -= 1

#display the text on different buttons
def TextDisplay(screen, text, text_font, text_x, text_y):
     text_img = pygame.font.Font.render(text_font, text, True, ('white'))
     screen.blit(text_img, (text_x,text_y))

def checkUpgrades(B1_rect, B2_rect, B3_rect, L1_speed, L2_speed, L3_speed, mouse):
    if B1_rect.collidepoint(mouse):
        print("button pressed")
        buttonUpgrades('L1', L1_speed)
        print(L1_speed)
                
    if B2_rect.collidepoint(mouse):
        buttonUpgrades('L2', L2_speed)
            
    if B3_rect.collidepoint(mouse):
        buttonUpgrades('L3', L3_speed)

#Tax the player for half of their money if they roll the TAXES value
def taxes(user_money, TAXES):
    # 1/TAXES chance for taxes each tick
    taxnum = random.randint(0,TAXES) 

    # if they roll taxes (the top value)
    if taxnum == TAXES: 
        #take half of their money and increase the tax counter on screen
        user_money = user_money/2 
        #taxcounter += 1 #TODO create the taxcounter on the screen
    
    #don't change the user money if they don't roll taxes
    
    #return the money back to the user, taxed or not
    return(user_money)