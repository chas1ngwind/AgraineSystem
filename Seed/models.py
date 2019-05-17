from django.db import models

# Create your models here.

class RoleInfo(models.Model):
    # set role
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.role

class DetailInfo(models.Model):
    amount = models.IntegerField(null=True)
    type = models.CharField(max_length=10)
    generation = models.CharField(max_length=10)
    name = models.CharField(max_length=10, null=True)
    contactnumber = models.IntegerField(null=True)
    role = models.ForeignKey(RoleInfo, on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.type
