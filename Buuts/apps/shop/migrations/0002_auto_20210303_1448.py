# Generated by Django 3.1.4 on 2021-03-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='Name'),
        ),
    ]
