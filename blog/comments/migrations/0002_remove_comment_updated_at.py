# Generated by Django 5.1.2 on 2024-11-04 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="updated_at",
        ),
    ]
