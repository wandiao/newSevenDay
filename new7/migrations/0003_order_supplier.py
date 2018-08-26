# Generated by Django 2.1 on 2018-08-25 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0002_auto_20180825_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(blank=True, help_text='供应商', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Supplier', verbose_name='供应商'),
        ),
    ]
