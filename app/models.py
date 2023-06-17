from django.db import models


# Create your models here.

# 药品
class Drug(models.Model):
    """药品"""
    drugname = models.CharField(verbose_name='药品名称', max_length=32)
    drugjixing = models.CharField(verbose_name='剂型', max_length=32)
    drugcate = models.CharField(verbose_name='分类', max_length=32, null=True, blank=True)
    money = models.DecimalField(verbose_name='单价', max_digits=10, decimal_places=2, default=0)
    number = models.IntegerField(verbose_name='库存数量')
    drugspe = models.CharField(verbose_name='规格', max_length=32)
    produce = models.CharField(verbose_name='生产企业', max_length=32)
    insure_choices = (
        (1, '基本药物保险'),
        (2, '大病药品保险'),
        (3, '补充药品保险'),
        (4, '商业药品保险')
    )
    insure = models.SmallIntegerField(verbose_name="医疗保险类型", choices=insure_choices, default=1)
    drugrat = models.CharField(verbose_name='批准文号', max_length=64)
    drugant_choices = (
        (1, '非抗菌'),
        (2, '抗生素'),
        (3, '抗真菌药物'),
        (4, '抗病毒药物'),
        (5, '抗寄生虫药物'),
        (6, '抗结核药物'),
        (7, '抗原虫药物'),
    )
    drugant = models.SmallIntegerField(verbose_name="抗菌类别", choices=drugant_choices, default=1)
    drugnid = models.CharField(verbose_name='药品类型编码', max_length=64)
    drugkey_choices = ((1, '是'), (2, '否'))
    drugkey = models.SmallIntegerField(verbose_name='重点关注药品', choices=drugkey_choices, default=2)
    drugun_choices = ((1, '通过'), (2, '未通过'))
    drugun = models.SmallIntegerField(verbose_name='一致性评价', choices=drugun_choices, default=2)


# 员工
class Work(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=256)
    time = models.DateField(verbose_name='入职时间')
    name = models.CharField(verbose_name="姓名", max_length=64)
    phone = models.CharField(verbose_name="电话", max_length=64)
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


# 管理员
class Admin(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=256)


# 普通用户
class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=256)


# 出库
class ChuKu(models.Model):
    drug_name = models.CharField(verbose_name='药品名称', max_length=32)
    out_money = models.DecimalField(verbose_name='售出总价', max_digits=10, decimal_places=2, default=0)
    out_number = models.IntegerField(verbose_name='出库数量', null=True, blank=True)
    out_time = models.DateField(verbose_name='出库时间', null=True, blank=True)


# 入库

class RuKu(models.Model):
    drug_name = models.CharField(verbose_name='药品名称', max_length=32)
    in_money = models.DecimalField(verbose_name='购买总价', max_digits=10, decimal_places=2, default=0)
    in_number = models.IntegerField(verbose_name='入库数量', null=True, blank=True)
    in_time = models.DateField(verbose_name='入库时间', null=True, blank=True)

