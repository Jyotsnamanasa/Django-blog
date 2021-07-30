from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', views.PostList.as_view(), name='home'),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]