# Generated by Django 4.2.1 on 2023-05-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0015_ruku"),
    ]

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("useradmin", models.CharField(max_length=32, verbose_name="用户名")),
                ("pwd", models.CharField(max_length=64, verbose_name="密码")),
            ],
        ),
    ]
