import datetime

from django.db import models

# Create your models here.
class RemittanceRow(models.Model):
    date=models.DateField(default=datetime.date.today)

    #
    # master_image = models.ImageField(upload_to=upload_about_us_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    class Meta:
        verbose_name = 'حواله انبار'
        verbose_name_plural = 'حواله های انبار'




    def __str__(self):
        return str(self.id)