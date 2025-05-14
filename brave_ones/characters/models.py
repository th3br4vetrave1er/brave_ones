from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=100)  # Character name
    race = models.CharField(max_length=50)   # Race
    character_class = models.CharField(max_length=50)  # Character class
    bio = models.TextField(blank=True)       # BIO
    created_at = models.DateTimeField(auto_now_add=True)  # Creation date

    def __str__(self):
        return self.name