# Generated by Django 5.0.4 on 2024-05-04 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_user_profile_pic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="city",
        ),
    ]
