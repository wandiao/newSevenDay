# Generated by Django 2.1 on 2018-10-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0013_auto_20181021_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsrecord',
            options={'verbose_name': '商品记录', 'verbose_name_plural': '商品记录'},
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, help_text='成本', max_digits=10, verbose_name='成本'),
        ),
    ]