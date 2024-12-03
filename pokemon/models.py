from django.db import models

class Pokemon(models.Model):
    poke_name = models.CharField(max_length=255)
    poke_type = models.CharField(max_length=255)

    def __str__(self):
        return self.poke_name
