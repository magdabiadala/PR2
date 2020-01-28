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

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
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

#def delete_user(request, id):
#    user = get_object_or_404(User, pk=id)
#    if form.is_valid():
#        user = form.save(commit=False)
#        user.is_deleted = True
#        user.save()
#        return redirect('/projekt/', pk=user.pk)

#    user.is_deleted = True
#    return HttpResponseRedirect('/projekt/')
