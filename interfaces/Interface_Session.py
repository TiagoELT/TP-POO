# session_id,user_id,timestamp_login,timestamp_logout
class Session():
    def __init__(self, session_id: int, user_id: int, timestamp_login: str, timestamp_logout: str) -> None:
        self.session_id = session_id
        self.user_id = user_id
        self.timestamp_login = timestamp_login
        self.timestamp_logout = timestamp_logout