import pandas as pd
import math
import random
from GameElementBase import GameElementBase
from MapArea import MapArea
class MapAreas(GameElementBase):
    def __init__(self):
        self.mapdata = pd.read_excel(open('../Data/MapAreas.xlsx', 'rb'))
        num_rows = num_cols= math.ceil(math.sqrt(self.mapdata.shape[0]))
        self.maparray={}
        mapdatacopy=self.mapdata.copy()
        for i in range(num_rows):
            for j in range(num_cols):
                if mapdatacopy.shape[0]==0:
                    break
                ind = random.randrange(mapdatacopy.shape[0])
                maparea = MapArea([i,j],mapdatacopy.iloc[ind])
                mapdatacopy.drop(mapdatacopy.index[ind], inplace=True)
                self.maparray[maparea.getPositionIndex()]=maparea
        
    def getRoomID(self,position):
        key = str(position[0])+"_"+str(position[1])
        return self.maparray[key].getRoomID()
    def getRoomName(self,position):
        key = str(position[0])+"_"+str(position[1])
        return self.maparray[key].getRoomName()
    def getRoom(self,position):
        key = str(position[0])+"_"+str(position[1])
        return self.maparray[key]
    def getMapData(self):
        return self.mapdata
    def getMapArray(self):
        return self.maparray