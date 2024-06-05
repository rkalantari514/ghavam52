import datetime

from django.db import models

from sale.models import Kala


# Create your models here.
class Havaleh(models.Model):
    date=models.DateField(default=datetime.date.today)

    #
    # master_image = models.ImageField(upload_to=upload_about_us_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    class Meta:
        verbose_name = 'حواله انبار'
        verbose_name_plural = 'حواله های انبار'




    def __str__(self):
        return str(self.id)

class HavalehRow(models.Model):
    numberin=models.IntegerField(default=0,verbose_name='تعداد ورود', null=True, blank=True)
    remittance=models.ForeignKey(Havaleh, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='حواله')
    kala=models.ForeignKey(Kala, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='کالا')


    #
    # master_image = models.ImageField(upload_to=upload_about_us_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    class Meta:
        verbose_name = 'ردیف حواله انبار'
        verbose_name_plural = 'ردیف های حواله انبار'




    def __str__(self):
        return str(self.id)