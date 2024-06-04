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


    #
    # master_image = models.ImageField(upload_to=upload_about_us_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'

    def __str__(self):
        return self.name

