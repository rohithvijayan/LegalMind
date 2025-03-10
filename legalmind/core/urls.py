from django.urls import path, re_path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("ragbot",views.ragbot,name='ragbot'),
    path("legalbot",views.legalbot,name='legalbot'),
    path("signup",views.register_page,name='signup_page'),
    path("login",views.login_page,name='login_page'),
    path("features",views.features,name='features'),
    path("api/ragchat/",views.ragchat,name='ragchat'),
    path("api/uploadFile/",views.fileHandler,name='uploadFile'),
    path("api/process/",views.embedder,name='process'),
    path("api/register/",views.register,name='register'),
    path("api/signin/",views.signin,name='signin'),
    path("logout",views.signout,name='logout'),
    path('docgen', views.select_document, name='select_document'),
    path('<str:doc_type>/', views.generate_document, name='generate_document'),
    path('categories/<str:category_name>/', views.category_documents, name='category_documents'),

]