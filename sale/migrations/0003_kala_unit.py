# Generated by Django 5.0.6 on 2024-06-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_kala_code_kala_kala_last_price_kala_last_price_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='kala',
            name='unit',
            field=models.CharField(default='دستگاه', max_length=150, verbose_name='واحد'),
        ),
    ]
