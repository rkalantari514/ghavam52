from django.db import models

# Create your models here.

class Producer(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    name = models.CharField(max_length=150, verbose_name='نام تولید کننده')
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)
    email = models.TextField(verbose_name='ایمیل', null=True, blank=True)
    phone = models.TextField(verbose_name='تلفن', null=True, blank=True)
    class Meta:
        verbose_name = 'تولید کننده'
        verbose_name_plural = 'تولید کننده ها'

    def __str__(self):
        return self.name

class Kinde_Kala(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    name = models.CharField(max_length=150, verbose_name='نوع کالا')

    class Meta:
        verbose_name = 'نوع کالا'
        verbose_name_plural = 'انواع کالا'

    def __str__(self):
        return self.name

class Kala(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    code_kala=models.IntegerField(verbose_name='کد کالا', null=True, blank=True)
    name = models.CharField(max_length=150, verbose_name='نام کالا')
    unit = models.CharField(default='دستگاه',max_length=150, verbose_name='واحد')
    producer=models.ForeignKey(Producer, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='تولید کننده')
    kinde_kala=models.ForeignKey(Kinde_Kala, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='نوع کالا')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    last_price=models.IntegerField(verbose_name='آخرین قیمت', null=True, blank=True)
    last_price_des = models.CharField(max_length=150, verbose_name='توضیحات آخرین قیمت')
    stock=models.IntegerField(default=0,verbose_name='موجودی انبار', null=True, blank=True)
    is_rl = models.BooleanField(default=False, verbose_name='راست و چپ دارد')
    stockr=models.IntegerField(default=0,verbose_name=' موجودی انبار راست', null=True, blank=True)
    stockl=models.IntegerField(default=0,verbose_name='موجودی انبار چپ', null=True, blank=True)


    #
    # master_image = models.ImageField(upload_to=upload_about_us_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'

    def save(self, *args, **kwargs):
        super().save()
        if self.is_rl:
            self.stock=self.stockl+self.stockr
            super().save()



    def __str__(self):
        return self.name
class Customer(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    code=models.IntegerField(verbose_name='کد مشتری', null=True, blank=True)
    title1 = models.CharField(max_length=150,default='جناب آقای', verbose_name='عنوان مشتری 1', null=True, blank=True)
    name1 = models.CharField(max_length=150, verbose_name='نام مشتری 1', null=True, blank=True)
    title2 = models.CharField(max_length=150,default='مدیر عامل محترم شرکت', verbose_name='عنوان مشتری 2', null=True, blank=True)
    name2 = models.CharField(max_length=150, verbose_name='نام مشتری 2', null=True, blank=True)
    phone1 = models.CharField(max_length=150,verbose_name='1 تلفن', null=True, blank=True)
    phone2 = models.CharField(max_length=150,verbose_name='2 تلفن', null=True, blank=True)
    fax = models.CharField(max_length=150,verbose_name='فکس', null=True, blank=True)
    mobile1 = models.CharField(max_length=150,verbose_name='موبایل 1', null=True, blank=True)
    mobile2 = models.CharField(max_length=150,verbose_name='موبایل 2', null=True, blank=True)
    email=models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    address = models.CharField(max_length=300, verbose_name='آدرس', null=True, blank=True)
    website=models.CharField(max_length=150, verbose_name='وب سایت', null=True, blank=True)
    shenase=models.CharField(max_length=150, verbose_name='شناسه ملی', null=True, blank=True)

    rname1 = models.CharField(max_length=150, verbose_name='فرد مرتبط 1', null=True, blank=True)
    rphone1 = models.CharField(max_length=150,verbose_name='تلفن فرد مرتبط 1', null=True, blank=True)
    rname2 = models.CharField(max_length=150, verbose_name='فرد مرتبط 2', null=True, blank=True)
    rphone2 = models.CharField(max_length=150,verbose_name='تلفن فرد مرتبط 2', null=True, blank=True)
    rname3 = models.CharField(max_length=150, verbose_name='فرد مرتبط 3', null=True, blank=True)
    rphone3 = models.CharField(max_length=150,verbose_name='تلفن فرد مرتبط 3', null=True, blank=True)
    rname4 = models.CharField(max_length=150, verbose_name='فرد مرتبط 4', null=True, blank=True)
    rphone4 = models.CharField(max_length=150,verbose_name='تلفن فرد مرتبط 4', null=True, blank=True)
    rname5 = models.CharField(max_length=150, verbose_name='فرد مرتبط 5', null=True, blank=True)
    rphone6 = models.CharField(max_length=150,verbose_name='تلفن فرد مرتبط 5', null=True, blank=True)



    #
    # master_image = models.ImageField(upload_to=upload_about_us_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'

    def __str__(self):
        return f'{self.name1} {self.name2}'
