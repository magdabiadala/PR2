# Generated by Django 2.2.6 on 2020-01-14 16:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0004_auto_20200114_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date of birth'),
        ),
    ]