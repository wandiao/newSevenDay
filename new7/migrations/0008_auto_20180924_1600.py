# Generated by Django 2.1 on 2018-09-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0007_profile_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='desc',
            field=models.CharField(blank=True, help_text='描述', max_length=100, null=True, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='profile',
            name='desc',
            field=models.CharField(blank=True, help_text='描述', max_length=100, null=True, verbose_name='描述'),
        ),
    ]