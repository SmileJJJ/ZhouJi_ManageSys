from django.db import models

# Create your models here.
class company_member(models.Model):
    name = models.CharField(max_length=10,verbose_name='成员姓名')
    gender = models.CharField(max_length=5,verbose_name='成员性别')
    age = models.SmallIntegerField(verbose_name='成员年龄')
    birthday = models.DateField(verbose_name='出生日期')
    phone = models.CharField(max_length=15,verbose_name='联系方式')
    email = models.EmailField(verbose_name='电子邮箱')
    introduce = models.TextField(verbose_name='成员介绍')
    password = models.CharField(max_length=12,verbose_name='登录密码',default='123456')

    class Meta:
        db_table = 'company_member'
        verbose_name = '公司成员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_info(self):
        dic = {
            'id':self.id,
            'name':self.name,
            'gender':self.gender,
            'age':self.age,
            'birthday':self.birthday,
            'phone':self.phone,
            'email':self.email,
            'introduce':self.introduce,
        }
        return dic

class customer_info(models.Model):
    name = models.CharField(max_length=10,verbose_name='客户姓名')
    contact = models.CharField(max_length=30,verbose_name='联系方式')
    company = models.CharField(max_length=20,verbose_name='公司名称')
    business_introduce = models.TextField(verbose_name='业务介绍')
    receptionist = models.ForeignKey(company_member,on_delete=models.CASCADE,null=True,verbose_name='对接人员')
    remark = models.TextField(verbose_name='备注')

    class Meta:
        db_table = 'customer_info'
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class supplier_info(models.Model):
    name = models.CharField(max_length=10,verbose_name='供应商姓名')
    contact = models.CharField(max_length=30,verbose_name='联系方式')
    company = models.CharField(max_length=20,verbose_name='公司名称')
    business_introduce = models.TextField(verbose_name='业务介绍')
    receptionist = models.ForeignKey(company_member,on_delete=models.CASCADE, null=True,verbose_name='对接人员')
    remark = models.TextField(verbose_name='备注')

    class Meta:
        db_table = 'supplier_info'
        verbose_name = '供应商信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class factory_info(models.Model):
    name = models.CharField(max_length=10,verbose_name='工厂姓名')
    contact = models.CharField(max_length=30,verbose_name='联系方式')
    company = models.CharField(max_length=20,verbose_name='公司名称')
    business_introduce = models.TextField(verbose_name='业务介绍')
    receptionist = models.ForeignKey(company_member,on_delete=models.CASCADE, null=True,verbose_name='对接人员')
    remark = models.TextField(verbose_name='备注')

    class Meta:
        db_table = 'factory_info'
        verbose_name = '工厂信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




