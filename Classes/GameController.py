from StaticController import StaticController
def performAction(action):
    StaticController.playerCharacter.move(action)
        
    
def performEffect():
    StaticController.getEffectSlice()

while(True):
    #Produce Output
    performEffect()
    action = input()
    performAction(action)
    #Perform Action
    #Update ActionConsequences
    