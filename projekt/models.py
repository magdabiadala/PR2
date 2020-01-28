import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField('name', max_length=30)
    surname = models.CharField('surname', max_length=30, default="surname")
    date_of_birth = models.DateField('date of birth', default=timezone.now)
    login = models.CharField('login', max_length=30, default="login")
    is_deleted = models.BooleanField('is_deleted', default=False)

    def __str__(self):
        return self.name

    def delete_user(self):
        self.is_deleted = True
        self.save()



'''def delete_user(request, id):
    User.objects.get(id).delete()
    return HttpResponseRedirect('/')'''
