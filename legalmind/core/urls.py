from django.urls import path, re_path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("ragbot",views.ragbot,name='ragbot'),
    path("signup",views.register,name='signup'),
    path("login",views.login,name='login'),
    path("api/ragchat/",views.ragchat,name='ragchat')
]