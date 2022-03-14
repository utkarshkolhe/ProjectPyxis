import pandas as pd
from MapAreas import MapAreas
from PlayerCharacter import PlayerCharacter
from NonPlayerCharacter import NonPlayerCharacter
from random import randrange
import os.path
def customexec(code):
    exec('global i; i = %s' % code)
    global i
    return i
class StaticController:
    gameMap= MapAreas()
    variableMap = gameMap.getKeyMap()
    playerCharacter = PlayerCharacter([2,2])
    npcCharacter = NonPlayerCharacter([1,1])
    dialogData = pd.read_excel(open(os.path.dirname(__file__)+'/../Data/CommonDialogs.xlsx', 'rb'))
    effectData = pd.read_excel(open(os.path.dirname(__file__)+'/../Data/EffectMap.xlsx', 'rb'))
    playerUseCases = pd.read_excel(open(os.path.dirname(__file__)+'/../Data/PlayerUseCases.xlsx', 'rb'))
    @staticmethod
    def displayCD(tag,fillers):
        slice1=StaticController.dialogData[StaticController.dialogData["DialogTag"]==tag]
        picker = randrange(slice1.shape[0])
        dialog = slice1.iloc[picker]["Dialog"]
        dialog = dialog.format(**fillers)
        return dialog
    @staticmethod
    def deciepherPostConditions(conditionstr,tag="None"):
        conditionstr = str(conditionstr)
        debugflag= False
        if tag=="user-death-by-knife" or tag=="user-death-by-gun":
            debugflag=True
        conditions = conditionstr.strip().split("\n")
        msgs=[]
        
        if len(conditions)==0:
            return msgs
        for condition in conditions:
            conditiontemp = condition.replace("displayCD", "StaticController.displayCD")
            conditiontemp = conditiontemp.replace("variableMap", "StaticController.variableMap")
            conditiontemp = conditiontemp.replace("playerCharacter", "StaticController.playerCharacter")
            conditiontemp = conditiontemp.replace("npcCharacter", "StaticController.npcCharacter")
            conditiontemp = conditiontemp.replace("npcintheroom", "StaticController.npcintheroom")
            try:
                msg = customexec(conditiontemp)
                if debugflag:
                    print("Passed",conditiontemp)
                if type(msg)== type("s"):
                    msgs.append(msg)
            except:
                if debugflag:
                    print("Failed",conditiontemp)
                tempflag=False

        return msgs
    
    @staticmethod
    def deciepherPreConditions(conditionstr,tag="None"):
        conditionstr = str(conditionstr)
        conditions = conditionstr.strip().split("\n")
        debugflag=False
        if tag=="user-death-by-knife" or tag=="user-death-by-gun":
            debugflag=True
        if len(conditions)==0 or conditions[0]=="nan":
            return True
        flag=True
        for condition in conditions:
            conditiontemp = condition.replace("variableMap", "StaticController.variableMap")
            conditiontemp = conditiontemp.replace("playerCharacter", "StaticController.playerCharacter")
            conditiontemp = conditiontemp.replace("npcCharacter", "StaticController.npcCharacter")
            tempflag = False
            try:
                tempflag = eval(conditiontemp)
                if debugflag:
                    print(tempflag,conditiontemp)
            except:
                tempflag=False
                if debugflag:
                    print("FAILED",conditiontemp)
            flag = flag and tempflag
        return flag
    
    @staticmethod
    def getEffectSlice():
        array_of_msgs = []
        for ind,row in StaticController.effectData.iterrows():
            if row["MAX_SHOWN"] ==-1:
                flag = StaticController.deciepherPreConditions(row["Preconditions"],row["effect-tag"])
            elif row["MAX_SHOWN"] <= row["SHOWN"]:
                flag=False
            else:
                flag = StaticController.deciepherPreConditions(row["Preconditions"],row["effect-tag"])
                
                
            if flag:
                show = False
                if row["MAX_SHOWN"]==-1:
                    show = True
                elif row["SHOWN"]< row["MAX_SHOWN"]:
                    show=True
                if row["PROBABILTY"] > randrange(100):
                    show = True
                else:
                    show=False
                if show:
                    StaticController.effectData.loc[StaticController.effectData["EffectID"]==row["EffectID"],"SHOWN"]= row["SHOWN"]+1
                    msgs= StaticController.deciepherPostConditions(row["Postconditions"],row["effect-tag"])
                    array_of_msgs.append(msgs)
            
        return array_of_msgs
    @staticmethod
    def npcintheroom():
        if StaticController.playerCharacter.getRoom().getRoomName()== StaticController.npcCharacter.getRoom().getRoomName():
            return StaticController.displayCD("npc-in-room",{"npcname":StaticController.npcCharacter.getName()})
    
        return 0
    
    