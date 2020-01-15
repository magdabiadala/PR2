from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import User

def index(request):
    all_users = User.objects.all().order_by('id')
    context = {'all_users': all_users}
    return render(request, 'projekt/index.html', context)

def detail(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'projekt/detail.html', {'user': user})

def add_user(request):
    User(name = request.POST['name']).save()
#    User(surname = request.POST['surname']).save()
    return HttpResponseRedirect('/projekt/')

def delete_user(request, id):
    User.objects.get(id=id).delete()
    return HttpResponseRedirect('/projekt/')

def comlete_user(request, id):
    user = User.objects.get(id=id)
    user.is_deleted = False
    user.save()
    return HttpResponseRedirect('/')
