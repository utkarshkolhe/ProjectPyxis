from GameElementBase import GameElementBase
from random import randrange
class MapArea(GameElementBase):
    keymap={}
    def __init__(self,position,row_data):
        self.position = position
        self.visitcount=0
        self.inv=[]
        self.nodes=[]
        self.roomid = row_data["RoomID"]
        self.roomname = row_data["Name"]
        self.description = row_data["Description"]
        if str(row_data["Items"]) != "nan":
            items = str(row_data["Items"]).split(" ")
            for item in items:
                itemsize=item.split("%")
                if randrange(100)<int(itemsize[1]):
                    self.inv.append(itemsize[0])
        if str(row_data["Nodes"]) != "nan":
            items = str(row_data["Nodes"]).split(" ")
            for item in items:
                itemsize=item.split("%")
                
                if randrange(100)<int(itemsize[1]):
                    self.nodes.append(itemsize[0])
                    if itemsize[2]=="false":
                        self.keymap[itemsize[0].upper() +"_" +"ACTIVE"] = False
                    else:
                        self.keymap[itemsize[0].upper() +"_" +"ACTIVE"] = True
    def getKeyMap(self):
        return self.keymap
    def getRoomID(self):
        return self.roomid
    def getRoomName(self):
        return self.roomname
    def getDescription(self):
        return self.description
    def getPositionIndex(self):
        return str(self.position[0])+"_"+str(self.position[1])
    def getVisitCount(self):
        return self.visitcount
    def addVisit(self):
        self.visitcount+=1
    def hasObject(self,objectname):
        for item in self.inv:
            if item == objectname:
                return True
        return False
    def takeObject(self,objectname):
        self.inv.remove(objectname)
    def putObject(self,objectname):
        self.inv.append(objectname)
    def getDescription(self):
        return self.description

    def getItemDescription(self):
        from StaticController import StaticController
        if len(self.inv)==0:
            return 0
        elif len(self.inv)==1:
            itemstr = self.inv[0]
        else:
            itemstr = ""
            lenitems=len(self.inv)
            itemstr += self.inv[0]
            for i in range(1,lenitems-1):
                itemstr+= ", " +self.inv[i]
            itemstr+= " and " +self.inv[lenitems-1]
        return StaticController.displayCD("room-item-description",{"itemstr" : itemstr})
    def getNodeDescription(self):
        from StaticController import StaticController
        if len(self.nodes)==0:
            return 0
        answerstring=""
        print(self.nodes)
        for node in self.nodes:
            if (node.upper() +"_" +"ACTIVE") in StaticController.variableMap and StaticController.variableMap[node.upper() +"_" +"ACTIVE"] == True:
                answerstring+=StaticController.displayCD("room-active-node",{"nodename" : node})
            else:
                answerstring+=StaticController.displayCD("room-inactive-node",{"nodename" : node})
        return answerstring