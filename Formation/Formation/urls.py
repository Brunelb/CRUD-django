"""
URL configuration for Formation project.

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
from django.contrib import admin
from django.urls import path
from products.views import product_list, product_create, product_update, product_table,product_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',product_list,name='product_list'),
    path('create',product_create,name='product_create'),
    path('update/<int:my_id>',product_update,name='product_update'),
    path('delete/<int:my_id>',product_delete,name='product_delete'),
    path('table',product_table,name='product_table'),

]
