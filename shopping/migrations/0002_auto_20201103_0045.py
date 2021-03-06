# Generated by Django 3.1.3 on 2020-11-03 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='shirt_size',
            new_name='size',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='name',
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='payment_name',
            field=models.CharField(default='', max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='img_path',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='color',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shopping.product'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shopping.product'),
        ),
    ]
