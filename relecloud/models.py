from django.db import models
from django.urls import reverse

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    slug = models.SlugField()

    image = models.ImageField(
        upload_to='images/',
        default='images/imagenDefault.jpg')
    
    def __str__(self) -> str:
        return self.name
    
class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    destinations = models.ManyToManyField(
        Destination,
        related_name='cruises'
    )
    def __str__(self):
        return self.name

class InfoRequest(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.EmailField()
    notes = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    cruise = models.ForeignKey(
        Cruise,
        on_delete=models.PROTECT
    )

class Opinion(models.Model):
    title = models.CharField(max_length=200)
    opinion_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cruise = models.ForeignKey(
        'Cruise',
        on_delete=models.CASCADE,
        related_name='opinions'
    )

    def __str__(self):
        return self.title

