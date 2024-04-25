from helps.common.pico import Picohelps

class Nanohelps(Picohelps):
    
    def generateUniqueCode(self, pattern):
        # CMPTP-20240114123559618137
        return f'{pattern}-{self.getUniqueCodePattern()}'