# Generated by Django 2.2.6 on 2020-01-14 15:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0003_auto_20200114_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2020, 1, 14, 15, 14, 56, 488152, tzinfo=utc), verbose_name='date of birth'),
        ),
    ]