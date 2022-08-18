import datetime
from pickle import TRUE
from django.db import models

# Create your models here.


class Branches(models.Model):
    id = models.AutoField(auto_created=True, primary_key=TRUE)
    name = models.CharField(max_length=500, blank=False, null=False)
    lat = models.TextField()
    long = models.TextField()
    address = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateTimeField(default=datetime.datetime.now())

    # def __str__(self):
    #     return self.name + ' - ' + self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lat": self.lat,
            "long": self.long,
            "address": self.address,
            "date": self.date,
        }


class Feedbacks(models.Model):
    id = models.AutoField(auto_created=True, primary_key=TRUE)
    customer_full_name = models.CharField(
        max_length=500, blank=False, null=False)
    email_address = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now())

    # def __str__(self):
    #     return self.name + ' - ' + self.name

    def serialize(self):
        return {
            "id": self.id,
            "names": self.customer_full_name,
            "email": self.email_address,
            "phone_number": self.phone_number,
            "message": self.message,
            "date": self.date,
        }
