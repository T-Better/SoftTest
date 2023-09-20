from api.login import IhrmLogin


class BaseApi():
    def __init__(self):
        self.login_api = IhrmLogin()


