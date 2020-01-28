"""PR2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from projekt.views import delete_user
from projekt.views import add_user
#from projekt.views import add
#from projekt.views import edit
from projekt.views import edit_user

urlpatterns = [
    path('projekt/', include('projekt.urls')),
    path('delete_user/<int:id>/', delete_user),
    path('add_user/', add_user),
    #path('add/', add),
    #path('edit/<int:id>/', edit),
    path('edit_user/<int:id>/', edit_user),
    path('admin/', admin.site.urls),
]
