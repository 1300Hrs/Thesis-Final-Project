# Generated by Django 4.1.7 on 2023-02-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_date_created_post_date_posted_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(null=True),
        ),
    ]
