import pandas as pd
from MapAreas import MapAreas
from PlayerCharacter import PlayerCharacter
from random import randrange
def customexec(code):
    exec('global i; i = %s' % code)
    global i
    return i
class StaticController:
    variableMap={}
    gameMap= MapAreas()
    playerCharacter = PlayerCharacter([2,2])
    dialogData = pd.read_excel(open('../Data/CommonDialogs.xlsx', 'rb'))
    effectData = pd.read_excel(open('../Data/EffectMap.xlsx', 'rb'))
    @staticmethod
    def displayCD(tag,fillers):
        print(tag)
        slice1=StaticController.dialogData[StaticController.dialogData["DialogTag"]==tag]
        print(slice1)
        picker = randrange(slice1.shape[0])
        print(picker)
        dialog = slice1.iloc[picker]["Dialog"]
        return dialog
    @staticmethod
    def deciepherPostConditions(conditionstr):
        conditionstr = str(conditionstr)
        conditions = conditionstr.strip().split("\n")
        msgs=[]
        if len(conditions)==0:
            return msgs
        for condition in conditions:
            conditiontemp = condition.replace("displayCD", "StaticController.displayCD")
            try:
                msg = customexec(conditiontemp)
                print(msg)
                msgs.append(msg)
            except:
                tempflag=False

        return msgs
    
    @staticmethod
    def deciepherPreConditions(conditionstr):
        conditionstr = str(conditionstr)
        conditions = conditionstr.strip().split("\n")
        print(conditions)
        if len(conditions)==0 or conditions[0]=="nan":
            return True
        flag=True
        for condition in conditions:
            conditiontemp = condition.replace("variableMap", "StaticController.variableMap")
            tempflag = False
            print("incondition")
            try:
                
                tempflag = eval(conditiontemp)
                print(conditiontemp,tempflag)
            except:
                print("FAILED",conditiontemp)
                tempflag=False
            flag = flag and tempflag
        return flag
    
    @staticmethod
    def getEffectSlice():
        flags=[]
        for ind,row in StaticController.effectData.iterrows():
            if row["MAX_SHOWN"] ==-1:
                flag = StaticController.deciepherPreConditions(row["Preconditions"])
            elif row["MAX_SHOWN"] <= row["SHOWN"]:
                flag=False
            else:
                flag = StaticController.deciepherPreConditions(row["Preconditions"])
            flags.append(flag)
        print(flags)
        slice1 = StaticController.effectData[flags]
        array_of_msgs = []
        for ind,row in slice1.iterrows():
            
            msgs= StaticController.deciepherPostConditions(row["Postconditions"])
            print(msgs)
            array_of_msgs.append(msgs)
        return array_of_msgs
            
    
    