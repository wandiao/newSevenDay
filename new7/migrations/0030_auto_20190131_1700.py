# Generated by Django 2.1 on 2019-01-31 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0029_auto_20190131_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsrecord',
            name='amount',
            field=models.FloatField(help_text='成本', verbose_name='成本'),
        ),
        migrations.AlterField(
            model_name='shopinventory',
            name='amount',
            field=models.FloatField(help_text='商品成本', verbose_name='商品成本'),
        ),
    ]
