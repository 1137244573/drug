# Generated by Django 4.2.1 on 2023-05-16 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_chdrug_delete_sold"),
    ]

    operations = [
        migrations.DeleteModel(name="Chdrug",),
    ]
