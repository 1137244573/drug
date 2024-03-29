# Generated by Django 4.2.1 on 2023-05-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_drug_drugcate"),
    ]

    operations = [
        migrations.CreateModel(
            name="Work",
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
                ("username", models.CharField(max_length=32, verbose_name="用户名")),
                ("password", models.CharField(max_length=64, verbose_name="密码")),
                ("time", models.DateField(verbose_name="入职时间")),
                ("name", models.CharField(max_length=64, verbose_name="姓名")),
                ("phone", models.CharField(max_length=64, verbose_name="电话")),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(1, "男"), (2, "女")], verbose_name="性别"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="drug",
            name="drugant",
            field=models.SmallIntegerField(
                choices=[
                    (1, "非抗菌"),
                    (2, "抗生素"),
                    (3, "抗真菌药物"),
                    (4, "抗病毒药物"),
                    (5, "抗寄生虫药物"),
                    (6, "抗结核药物"),
                    (7, "抗原虫药物"),
                ],
                default=1,
                verbose_name="抗菌类别",
            ),
        ),
    ]
