# Generated by Django 2.1 on 2018-09-23 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0002_auto_20180923_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordergoods',
            old_name='goods_id',
            new_name='goods',
        ),
        migrations.RenameField(
            model_name='ordergoods',
            old_name='order_id',
            new_name='order',
        ),
    ]