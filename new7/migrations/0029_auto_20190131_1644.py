# Generated by Django 2.1 on 2019-01-31 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0028_auto_20190108_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsrecord',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, help_text='成本', max_digits=10, verbose_name='成本'),
        ),
    ]
