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
        slice1=StaticController.dialogData[StaticController.dialogData["DialogTag"]==tag]
        picker = randrange(slice1.shape[0])
        dialog = slice1.iloc[picker]["Dialog"]
        dialog = dialog.format(**fillers)
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
            conditiontemp = conditiontemp.replace("variableMap", "StaticController.variableMap")
            try:
                msg = customexec(conditiontemp)
                if type(msg)== type("s"):
                    msgs.append(msg)
            except:
                tempflag=False

        return msgs
    
    @staticmethod
    def deciepherPreConditions(conditionstr):
        conditionstr = str(conditionstr)
        conditions = conditionstr.strip().split("\n")
        if len(conditions)==0 or conditions[0]=="nan":
            return True
        flag=True
        for condition in conditions:
            conditiontemp = condition.replace("variableMap", "StaticController.variableMap")
            tempflag = False
            try:
                tempflag = eval(conditiontemp)
            except:
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
        slice1 = StaticController.effectData[flags]
        
        #Logic for picking from SLICE
        slice1flags=[]
        for ind,row in slice1.iterrows():
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
                #row["SHOWN"]+=1
            slice1flags.append(show)
        
        slice2 = slice1[slice1flags]
        array_of_msgs = []
        for ind,row in slice2.iterrows():
            msgs= StaticController.deciepherPostConditions(row["Postconditions"])
            array_of_msgs.append(msgs)
        return array_of_msgs
            
    
    