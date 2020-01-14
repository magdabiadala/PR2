from django.urls import path

from . import views
from projekt.views import delete_user

app_name = 'projekt'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('delete_user/<int:id>/', delete_user),
]
