# Generated by Django 5.0.4 on 2024-05-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0004_remove_community_image_community_banner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="community",
            name="banner",
            field=models.ImageField(
                default="community/banner/banner.jpeg", upload_to="community/banner/"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="community",
            name="profile_image",
            field=models.ImageField(
                default="community/profile_image/ChessSet.jpg",
                upload_to="community/profile_image/",
            ),
            preserve_default=False,
        ),
    ]