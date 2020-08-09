from .user_model import BaseUser

class Client(BaseUser):
    def __str__(self):
        return str(self.user)
