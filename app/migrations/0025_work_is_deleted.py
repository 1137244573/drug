# Generated by Django 4.2.1 on 2023-06-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0024_delete_qing"),
    ]

    operations = [
        migrations.AddField(
            model_name="work",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
