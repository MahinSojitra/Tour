"""
URL configuration for myproject project.

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
from .views import (
    index as home_view_handler,
    services as services_view_handler,
    contact as contact_view_handler,
    about as about_view_handler,
    packageDetail as package_detail_view_handler,
    get_packages as packages_view_handler,
    user_signup as signup_view_handler,
    user_login as login_view_handler,
    user_logout as logout_view_handler,
    editprofile as edit_view_handler,
    book as book_view_handler,
    search as searchresult_view_handler
)

urlpatterns = [
    path('', home_view_handler, name='home_view'),
    path('services', services_view_handler, name='services_view'),
    path('contact',contact_view_handler,name='contact_view'),
    path('about', about_view_handler, name='about_view'),
    path('detail/<str:packageID>',package_detail_view_handler,name='package_detail_view'),
    path('packages',packages_view_handler,name='packages_view'),
    path('signup',signup_view_handler,name='signup_view'),
    path('login',login_view_handler,name='login_view'),
    path('logout',logout_view_handler,name='logout_view'),
    path('editprofile',edit_view_handler,name='edit_view'),
    path('book',book_view_handler,name='book_view'),
    path('result',searchresult_view_handler,name='searchresult_view'),
]
