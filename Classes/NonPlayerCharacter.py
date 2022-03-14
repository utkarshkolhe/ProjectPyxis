from LivingThings import LivingThings

class NonPlayerCharacter(LivingThings):
    def __init__(self,position):
        LivingThings.__init__(self, position,"NPC","Adrien","Crewmember Adrien")