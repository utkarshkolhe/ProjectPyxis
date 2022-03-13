from GameElementBase import GameElementBase
class MapArea(GameElementBase):
    def __init__(self,position,row_data):
        self.position = position
        self.visitcount=0
        self.inv=["gun"]
        self.interactables={}
        self.roomid = row_data["RoomID"]
        self.roomname = row_data["Name"]
        self.description = row_data["Description"]
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
        if objectname in self.inv:
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