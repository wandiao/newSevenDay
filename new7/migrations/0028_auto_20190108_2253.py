# Generated by Django 2.1 on 2019-01-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0027_auto_20190108_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsdamaged',
            name='amount',
            field=models.FloatField(default=0, help_text='损失成本', verbose_name='损失成本'),
        ),
        migrations.AlterField(
            model_name='goodsrecord',
            name='amount',
            field=models.FloatField(help_text='成本', verbose_name='成本'),
        ),
    ]
