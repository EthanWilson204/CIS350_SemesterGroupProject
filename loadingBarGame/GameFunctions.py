import random


#Tax the player for half of their money if they roll the TAXES value
def Taxes(user_money, TAXES):
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

def Stop_All():
    return 0, 0, 0, 1000000

def Upgrade_Bar(bar_comps):
    
    bar_speed, up_price, user_money = bar_comps
    bar_speed *= 1.3
    user_money -= up_price
    up_price *= 1.2
    
    return bar_speed, up_price, user_money