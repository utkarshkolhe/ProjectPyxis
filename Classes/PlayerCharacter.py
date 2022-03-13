from LivingThings import LivingThings

class PlayerCharacter(LivingThings):
    def __init__(self,position):
        LivingThings.__init__(self, position,"PLAYER","Olivia","Commander Olivia")
        