# Generated by Django 3.1.4 on 2021-03-03 14:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210303_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='heigth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Heigth'),
        ),
        migrations.AlterField(
            model_name='item',
            name='weigth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='weigth'),
        ),
        migrations.AlterField(
            model_name='item',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Width'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='count',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='salesend',
            name='cp',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='C.P'),
        ),
        migrations.AlterField(
            model_name='size',
            name='value',
            field=models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='Value'),
        ),
    ]