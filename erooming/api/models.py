from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

class Routine(models.Model):
    title = models.CharField(max_length=100)
    max_people_number = models.IntegerField()
    now_people_number = models.IntegerField()
    description = models.CharField(max_length=200)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    max_count = models.IntegerField()
    status = models.CharField(max_length=10)

class User_Routine(models.Model):
    user_id = models.IntegerField()
    routine_id = models.IntegerField()
    now_count = models.IntegerField()
    max_count = models.IntegerField()
    is_host = models.BooleanField()


# Create your models here.
