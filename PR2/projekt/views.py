from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import User

def index(request):
    latest_users_list = User.objects.order_by('-date_of_birth')[:5]
    context = {'latest_users_list': latest_users_list}
    return render(request, 'projekt/index.html', context)

def detail(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'projekt/detail.html', {'user': user})
