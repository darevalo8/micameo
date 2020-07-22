from micameo.users.helpers import RegisterUser
from micameo.users.models import Client


class RegisterClient(RegisterUser):
    model = Client
