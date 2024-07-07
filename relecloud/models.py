from django.db import models
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.db import models

# models.py
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

    image = models.ImageField(
        upload_to='res/img/',  # Remove 'static/' from here
        default='images/imagenDefault.jpg'
    )
    
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

    def __str__(self):
        return f'{self.name} - {self.email}'

    def send_notification_email(self):
        subject = f'New Information Request: {self.name}'
        message = f'Hello,\n\nA new information request has been submitted.\n\nName: {self.name}\nEmail: {self.email}\nNotes: {self.notes}\n\nPlease follow up with the customer regarding Cruise: {self.cruise.name}\n\nBest regards,\nYour Website Team'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [self.email]
        send_mail(subject, message, from_email, recipient_list)
        

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