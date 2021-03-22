# This code is a direct translation of the
# Rockstar code piece in the parent folder
# Thus, variable names are awful, logic is
# redundant and suboptimal for in exchange
# of pure beauty for the rockstar source.

def Death(Old, Young):
    while Old >= Young:
        Everyone = False
        Everyone = Old
        Old = Old - Young      
        Everyone = Old
        
    return Everyone
        
def Life(Everything):
    Fear = 1
    The_Sky = Everything - Fear
    Magic = 1
    while not Magic == The_Sky:
        Magic = Magic + 1
        if Death(Everything, Magic) == 0:
            return False                      
    return True

The_Boy = 100
His_Love = 2
while not His_Love > The_Boy:
    if Life(His_Love) == True:
        print(His_Love)
    His_Love = His_Love + 1
