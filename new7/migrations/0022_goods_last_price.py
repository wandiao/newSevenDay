# Generated by Django 2.1 on 2018-11-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0021_auto_20181103_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='last_price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='上次价格', max_digits=10, verbose_name='上次价格'),
        ),
    ]
