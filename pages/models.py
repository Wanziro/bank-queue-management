from calendar import month
from operator import truediv
from pickle import TRUE
from django.db import models

# Create your models here.


class QueueDetails(models.Model):
    id = models.AutoField(auto_created=True, primary_key=TRUE)
    name = models.CharField(max_length=30, blank=True, default="Anonymous")
    day = models.IntegerField(blank=False, null=False)
    month = models.IntegerField(blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    joinedTimeAndDate = models.TextField(blank=False, null=False)
    leaveTimeAndDate = models.TextField(blank=TRUE, null=True, default="-")
    status = models.CharField(max_length=100, blank=False, default="online")

    # def __str__(self):
    #     return self.name + ' - ' + self.status

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "day": self.day,
            "month": self.month,
            "year": self.year,
            "joinedTimeAndDate": self.joinedTimeAndDate,
            "leaveTimeAndDate": self.leaveTimeAndDate,
            "status": self.status,
        }
