# Generated by Django 2.1 on 2019-01-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0024_shopinventory_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.FloatField(default=0, help_text='库存', verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_count',
            field=models.FloatField(default=0, help_text='总数量', verbose_name='总数量'),
        ),
    ]
