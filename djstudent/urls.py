"""djstudent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path, include
from students import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create),
    path('', views.view),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    re_path(r'^import/excel/$', views.import_excel, name='import_xls'),
    re_path(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
    re_path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]
