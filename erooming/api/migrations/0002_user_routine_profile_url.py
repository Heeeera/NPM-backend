# Generated by Django 3.2.15 on 2022-08-22 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_routine',
            name='profile_url',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]