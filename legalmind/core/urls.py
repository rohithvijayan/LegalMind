from django.urls import path, re_path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("ragbot",views.ragbot,name='ragbot'),
    path("signup",views.register_page,name='signup_page'),
    path("login",views.login_page,name='login_page'),
    path("api/ragchat/",views.ragchat,name='ragchat'),
    path("api/uploadFile/",views.fileHandler,name='uploadFile'),
    path("api/process/",views.embedder,name='process'),
    path("api/register/",views.register,name='register'),
    path("api/signin/",views.signin,name='signin'),
    path("logout",views.signout,name='logout'),
]