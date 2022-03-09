from StaticController import StaticController
def performAction(action):
    StaticController.playerCharacter.move(action)
    
def conditionCheck(arg1,arg2,condition):
    if condition =="EQUAL":
        return arg1 == arg2
    if condition =="NOTEQUAL":
        return arg1 != arg2
    if condition =="GREATERTHAN":
        return arg1 > arg2
    
def deciepherPreConditions(conditionstr):
    conditions = conditionstr.strip().split("###")
    if len(conditions)==0:
        return True
    if conditions[0]=="EVAL"
    
            
        
    
def performEffect():
    

while(True):
    #Produce Output
    action = input()
    performAction(action)
    #Perform Action
    #Update ActionConsequences
    