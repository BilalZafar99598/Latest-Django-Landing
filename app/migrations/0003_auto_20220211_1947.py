# Generated by Django 3.2.9 on 2022-02-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='day_left',
        ),
        migrations.AddField(
            model_name='brand',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Expiry Date'),
        ),
        migrations.AddField(
            model_name='brand',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
