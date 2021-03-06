# Generated by Django 2.1 on 2019-01-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0026_auto_20190108_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depot',
            name='cubage',
            field=models.DecimalField(decimal_places=2, default=0, help_text='容量', max_digits=10, verbose_name='容量'),
        ),
        migrations.AlterField(
            model_name='depot',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=0, help_text='库存', max_digits=10, verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=0, help_text='库存', max_digits=10, verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='warn_stock',
            field=models.DecimalField(decimal_places=2, default=10, help_text='报警库存', max_digits=10, verbose_name='报警库存'),
        ),
        migrations.AlterField(
            model_name='goodsdamaged',
            name='count',
            field=models.DecimalField(decimal_places=2, help_text='数量', max_digits=10, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='goodsrecord',
            name='count',
            field=models.DecimalField(decimal_places=2, default=0, help_text='数量', max_digits=10, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='goodsrecord',
            name='leave_count',
            field=models.DecimalField(decimal_places=2, default=0, help_text='出库数量', max_digits=10, verbose_name='出库数量'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_count',
            field=models.DecimalField(decimal_places=2, default=0, help_text='总数量', max_digits=10, verbose_name='总数量'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='count',
            field=models.DecimalField(decimal_places=2, default=1, help_text='数量', max_digits=10, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='shopinventory',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=0, help_text='库存', max_digits=10, verbose_name='库存'),
        ),
    ]
