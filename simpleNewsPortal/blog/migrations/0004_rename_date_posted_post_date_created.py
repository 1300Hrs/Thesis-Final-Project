# Generated by Django 4.1.7 on 2023-02-25 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="date_posted",
            new_name="date_created",
        ),
    ]
