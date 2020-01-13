import datetime
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField('name', max_length=30)
    surname = models.CharField('surname', max_length=30)
    date_of_birth = models.DateField('date of birth')
    login = models.CharField('login', max_length=30)
    is_deleted = models.BooleanField('is_deleted', default=False)

    def __str__(self):
        return self.name

    def was_born_recently(self):
        return self.date_of_birth >= timezone.now() - datetime.timedelta(days=1)
