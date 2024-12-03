from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_login, name='user_logout'),
    path('sign_up/', views.signUp, name='user_signUp'),
    path('', views.profile, name='profile'),
]