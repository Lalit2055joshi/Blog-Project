from django.db import models
from django.forms import CharField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=500, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    image = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.address1}{self.address2}"
