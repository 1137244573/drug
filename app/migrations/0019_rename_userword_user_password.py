# Generated by Django 4.2.1 on 2023-05-20 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_rename_pwd_admin_password_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="userword", new_name="password",
        ),
    ]
