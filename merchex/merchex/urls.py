"""
URL configuration for merchex project.

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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.bands_list, name='band-list'),
    path('band/<int:id>/', views.band_detail, name='band-detail'),
    path('band/<int:id>/update', views.band_update, name='band-update'),
    path('band/<int:id>/delete', views.band_delete, name='band-delete'),
    path('band/add/', views.band_create, name='band-create'),
    path('news/', views.news_list, name='news-list'),
    path('new/<int:id>/', views.new_detail, name='new-detail'),
    path('new/<int:id>/update', views.new_update, name='new-update'),
    path('new/<int:id>/delete', views.new_delete, name='new-delete'),
    path('new/add/', views.new_create, name='new-create'),
    path('contact-us/', views.contact, name='contact'),
    path('email-sent/', views.email_sent, name='email-sent'),
]
