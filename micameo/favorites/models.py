from django.db import models
from micameo.users.models import Talent, Client


class Favorite(models.Model):
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.talent)
