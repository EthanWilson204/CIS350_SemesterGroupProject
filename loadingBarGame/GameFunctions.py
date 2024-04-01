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

