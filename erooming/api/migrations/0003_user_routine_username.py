# Generated by Django 3.2.15 on 2022-08-22 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_routine_profile_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_routine',
            name='username',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
