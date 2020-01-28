from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect

from .models import User
from .forms import UserForm

def index(request):
    all_users = User.objects.all().order_by('id')
    context = {'all_users': all_users}
    return render(request, 'projekt/index.html', context)

def detail(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'projekt/detail.html', {'user': user})

#widok
#def add(request):
#    return render(request, 'projekt/add.html')

#def add_user(request):
#    User(name = request.POST['name'], surname = request.POST['surname']).save()
#    return HttpResponseRedirect('/projekt/')

#funkcja
#def add_user(request):
#    form = UserForm()
#    User(name = request.POST['name']).save()
#    User(name = request.POST['name'], surname = request.POST['surname'], date_of_birth = request.POST['date_of_birth'], login = request.POST['login']).save()
#    context = {'user': user}
#    return HttpResponseRedirect('/projekt/')
#    return render(request, 'projekt/edit.html', {'form': form})

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
#            user.name = request.name
#            user.surname = request.surname
#            user.date_of_birth = request.date_of_birth
#            user.login = request.login
            user.is_deleted = False
            user.save()
            return redirect('/projekt/', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'projekt/edit.html', {'form': form})

def edit_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_deleted = False
            user.save()
            return redirect('/projekt/', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'projekt/edit.html', {'form': form})

#def edit(request, id):
#    user = get_object_or_404(User, pk=id)
#    return render(request, 'projekt/edit.html', {'user': user})

#def edit_user(request, id):
#    user = get_object_or_404(User, pk=id)
#    if request.method == "POST":
#            User(name = request.POST['name'], surname = request.POST['surname'], date_of_birth = request.POST['date_of_birth'], login = request.POST['login']).save()
#    return HttpResponseRedirect('/projekt/')

def delete_user(request, id):
    User.objects.get(id=id).delete()
    return HttpResponseRedirect('/projekt/')

def comlete_user(request, id):
    user = User.objects.get(id=id)
    user.is_deleted = False
    user.save()
    return HttpResponseRedirect('/')
