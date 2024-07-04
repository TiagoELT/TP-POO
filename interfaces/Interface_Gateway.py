class Gateway:
    def __init__(self, gateway_id: int, device_id: int, sim_card_iccid: str, imei: str) -> None:
        self.gateway_id = gateway_id
        self.device_id = device_id
        self.sim_card_iccid = sim_card_iccid
        self.imei = imei
