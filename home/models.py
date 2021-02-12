from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    phone = models.CharField(max_length=12)
    date = models.DateTimeField()


    def __str__(self):
        return self.name
    