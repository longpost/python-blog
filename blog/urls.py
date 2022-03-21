# -*- coding: utf-8 -*-


from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:post_id>/', views.detail, name='detail'),
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
]