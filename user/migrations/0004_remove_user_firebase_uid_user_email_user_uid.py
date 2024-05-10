# Generated by Django 5.0.4 on 2024-05-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_user_city"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="firebase_uid",
        ),
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(
                default="", editable=False, max_length=254, unique=True
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="uid",
            field=models.CharField(
                default="",
                editable=False,
                max_length=128,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
            preserve_default=False,
        ),
    ]