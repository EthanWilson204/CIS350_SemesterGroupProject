import random


#Tax the player for half of their money if they roll the TAXES value
def taxes(user_money, TAXES, taxPercent, tax_sfx):
    # 1/TAXES chance for taxes each tick
    taxnum = random.randint(0,TAXES) 
    taxDecimalMultiplier = 1 - (taxPercent / 100)
    # if they roll taxes (the top value)
    if taxnum == TAXES: 
        #take half of their money and increase the tax counter on screen
        user_money = user_money * taxDecimalMultiplier
        tax_sfx.play()
        #taxcounter += 1 #TODO create the taxcounter on the screen
    
    #don't change the user money if they don't roll taxes
    
    #return the money back to the user, taxed or not
    return(user_money)

def Add_Reset(bar_amt, bar_pos, start_pos, user_money):
    
    user_money += bar_amt
    bar_pos = start_pos
    
    return user_money, bar_pos

def Upgrade_Bar(bar_comps):
    
    bar_speed, up_price, user_money = bar_comps
    bar_speed *= 1.3
    user_money -= up_price
    up_price *= 1.2
    
    return bar_speed, up_price, user_money

def Start_Profit(amt_comps, multiplier):
    
    L1A, L2A, L3A, money, status1_active, stat_price = amt_comps
    
    money -= stat_price
    status1_active = True
    L1A *= multiplier
    L2A *= multiplier
    L3A *= multiplier
    
    return L1A, L2A, L3A, money, status1_active, stat_price

def Stop_Profit(stop_comps, multiplier):
    L1A, L2A, L3A, status1_active = stop_comps
    
    L1A /= multiplier
    L2A /= multiplier
    L3A /= multiplier
    status1_active = False
    
    return L1A, L2A, L3A, status1_active 

