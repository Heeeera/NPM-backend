from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
      return self.name


class Routine(models.Model):
    title = models.CharField(max_length=100)
    max_people_number = models.IntegerField(null=False)
    now_people_number = models.IntegerField(null=False)
    description = models.CharField(null=False, max_length=200)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    max_count = models.IntegerField(null=False)
    created_at = models.DateField(auto_now_add=True)  # auto_now는 수정일자, auto_now_add는 생성일자(불변)
    status = models.CharField(max_length=10)

    def __str__(self):
      return self.title


class User_Routine(models.Model):
    user_id = models.IntegerField()
    routine_id = models.IntegerField()
    now_count = models.IntegerField()
    max_count = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_host = models.BooleanField()
