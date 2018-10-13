from django.db import models

# Create your models here.
class GuardianInfo(models.Model):
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=30)
    gender_choice = (('m', 'Male'), ('f', 'Female'))
    gender = models.CharField(max_length = 20, choices=gender_choice)
    age = models.IntegerField()
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return (self.name)

class StudentsInfo(models.Model):
    name = models.CharField(max_length = 200)
    roll = models.IntegerField()
    std_class = models.IntegerField()
    gender_choice = (('m', 'Male'), ('f', 'Female'))
    gender = models.CharField(max_length = 50, choices = gender_choice)
    age = models.IntegerField()
    guardian = models.OneToOneField(GuardianInfo, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return(self.name)
