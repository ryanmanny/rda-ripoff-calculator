# Generated by Django 2.0.5 on 2018-07-14 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RipoffServer', '0004_auto_20180713_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ripoff',
            name='base_cost',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
