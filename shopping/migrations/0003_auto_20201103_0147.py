# Generated by Django 3.1.3 on 2020-11-03 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20201103_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='payment_methdos',
            field=models.ManyToManyField(blank=True, to='shopping.PaymentMethod'),
        ),
    ]