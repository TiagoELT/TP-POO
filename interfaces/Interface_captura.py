# captura_id,install_cage_id,timestamp,wildlife_id,user_id
from datetime import date
class Captura:
    def __init__(self, captura_id: int, install_cage_id: int, timestamp: date, wildlife_id: int, user_id: int) -> None:
        self.captura_id = captura_id
        self.install_cage_id = install_cage_id
        self.timestamp = timestamp
        self.wildlife_id = wildlife_id
        self.user_id = user_id