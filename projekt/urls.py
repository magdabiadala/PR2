from django.urls import path

from . import views
from . import models
from projekt.views import delete_user
from projekt.models import add_user
from projekt.views import edit_user

app_name = 'projekt'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('delete_user/<int:id>/', delete_user),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:id>/', views.edit_user, name='edit_user'),
]
