# Generated by Django 3.2.15 on 2023-12-25 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
    ]
