from datetime import date
class Install_Gateway:
    def __init__(self, install_id: int, gateway_id: int, area_id: int, user_id: int, data_in: date, data_out: date) -> None:
        self.install_id = install_id
        self.gateway_id = gateway_id
        self.area_id = area_id
        self.user_id = user_id
        self.data_in = data_in
        self.data_out = data_out