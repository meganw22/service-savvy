"""
URL configuration for project_savvy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from home import views as savvy_views
from my_tasks import views as my_tasks_views

urlpatterns = [
    path('', savvy_views.index, name='index'),
    path('', include("my_requests.urls"), name="my-request-urls"),
    path('tasks/', my_tasks_views.my_tasks, name='tasks'),
    path('admin/', admin.site.urls),
]
