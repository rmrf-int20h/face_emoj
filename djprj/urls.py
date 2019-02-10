"""djprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import server.views

urlpatterns = [
    path("", server.views.index, name="index"),
    path('db_managment/', server.views.db_managment, name='db_managment'),
    path('db_create_table/', server.views.db_create_table, name='db_create_table'),
    path('db_delete_table/', server.views.db_delete_table, name='db_delete_table'),
    path('db_select_all/', server.views.db_select_all, name='db_select_all'),
    path('db_insert_row/', server.views.db_insert_row, name='db_insert_row'),
    path('db_select_emotions/', server.views.db_select_emotions, name='db_select_emotions')
]
