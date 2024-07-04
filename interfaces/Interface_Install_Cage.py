#install_id,cage_id,gateway_id,,user_id,data_in,data_out
from datetime import date
class Install_Cage:
    def __init__(self, install_id: int, cage_id: int, gateway_id: int, user_id: int, data_in: date, data_out: date):
        self.install_id = install_id
        self.cage_id = cage_id
        self.gateway_id = gateway_id
        self.user_id = user_id
        self.data_in = data_in
        self.data_out = data_out