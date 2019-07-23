from django.db import models
from datetime import datetime

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )


Choice = [
    ('music', 'Music'),
    ('play', 'Play'),
    ('dance', 'Dance'),
    ('party', 'Party'),
    ]

class Mood(models.Model):

    Team_Name = models.CharField(max_length=120)


    class Meta:
        db_table = "mood"



class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    file = models.FileField(upload_to='documents/', blank=True)

    def __str__(self):
        return self.title