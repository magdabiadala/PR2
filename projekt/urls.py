from django.urls import path

from . import views
from projekt.views import delete_user
from projekt.views import add_user
from projekt.views import add
from projekt.views import edit

app_name = 'projekt'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('delete_user/<int:id>/', delete_user),
    path('add_user/', views.add_user, name='add_user'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
]
