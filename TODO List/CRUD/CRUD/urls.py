"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin

from createOpr.views import base
from createOpr.views import delete
from createOpr.views import insertData
from createOpr.views import deleteData
from createOpr.views import updateData
from createOpr.views import showDataList
from createOpr.views import processDataDb
from login.views import loginPage

urlpatterns = [

    path('', base, name = 'Base'),
    path('Insert/', insertData, name='insert'),
    path('Show/', showDataList, name='showList'),
    path('Delete/', delete, name='delete'),
    path('Delete/<int:id>', deleteData, name='deleteRecord'),
    path('Update/<int:id>', updateData, name='updateRecord'),
    path('process/', processDataDb, name='processDB'),
    path('login/', loginPage, name='loginpage'),

    path('admin/', admin.site.urls),
]
