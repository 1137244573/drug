# Generated by Django 4.2.1 on 2023-05-20 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0017_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="admin", old_name="pwd", new_name="password",
        ),
        migrations.RenameField(
            model_name="admin", old_name="useradmin", new_name="username",
        ),
        migrations.RenameField(
            model_name="user", old_name="users", new_name="username",
        ),
        migrations.RenameField(
            model_name="user", old_name="userpwd", new_name="userword",
        ),
    ]
