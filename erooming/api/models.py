from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pk = models.IntegerField(blank=True)
    email = models.EmailField(max_length=500, blank=True)
    mygit = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to="profile/image", default='red.jpg')
    myInfo = models.CharField(max_length=150, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()