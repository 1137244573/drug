# Generated by Django 4.2.1 on 2023-05-16 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_inbound_rename_inouttime_outbound_outtime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outbound",
            name="outtime",
            field=models.DateField(blank=True, null=True, verbose_name="出库时间"),
        ),
    ]
