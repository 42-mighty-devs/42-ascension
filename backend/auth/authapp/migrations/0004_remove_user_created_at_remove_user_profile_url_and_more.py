# Generated by Django 5.1.5 on 2025-02-04 07:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authapp", "0003_delete_userinfo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="user",
            name="profile_url",
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
