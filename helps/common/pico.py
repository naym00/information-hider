from datetime import datetime
from datetime import date
class Picohelps:
    
    def getUniqueCodePattern(self):
        return f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"[:18]