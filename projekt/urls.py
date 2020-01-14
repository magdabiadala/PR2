from django.urls import path

from . import views
from projekt.views import deleteUser

app_name = 'projekt'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('deleteUser/<int:id>/', deleteUser),
]
