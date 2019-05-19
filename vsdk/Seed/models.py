from django.db import models

# Create your models here.

class RoleInfo(models.Model):
    # set role
    role = models.CharField(max_length=10)


    def __str__(self):
        return self.role

class DetailInfo(models.Model):
    id = models.IntegerField(primary_key = True)
    amount = models.IntegerField(null=True)
    type = models.CharField(max_length=10)
    generation = models.CharField(max_length=10)
    role = models.ForeignKey(RoleInfo, on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.type













# class SeedInfo(models.Model):
#     # set type
#     type = models.CharField(max_length=10)
#     selectRole = models.ForeignKey(RoleInfo, on_delete=models.CASCADE, default="")
#
#     def __str__(self):
#
#         return self.type
#
#
# class GenerationInfo(models.Model):
#     # set generation
#     generation = models.CharField(max_length=10)
#     role1 = models.ForeignKey(RoleInfo, on_delete=models.CASCADE, default="")
#     type1 = models.ForeignKey(SeedInfo, on_delete=models.CASCADE, default="")
#     def __str__(self):
#        return self.generation
#
#
#
# class DetailInfo(models.Model):
#     amount = models.IntegerField(default=0)
#     type = models.ForeignKey(SeedInfo, on_delete=models.CASCADE, default="")
#     generation = models.ForeignKey(GenerationInfo, on_delete=models.CASCADE, default="")
#     role = models.ForeignKey(RoleInfo, on_delete=models.CASCADE, default="")
#
#     def __int__(self):
#         return self.amount
