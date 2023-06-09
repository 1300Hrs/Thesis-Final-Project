# Generated by Django 4.1.7 on 2023-03-08 02:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0006_alter_category_options_post_image_post_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="blog_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
