from re import template
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from TecnoCoder import views
from TecnoCoder.views import NuevoBlog, Update_user_profile, Editar_Blog, Delete_Blog

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('nosotros', views.nosotros, name="Nosotros"),
    path('Blog', views.blog, name="Blog"),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='TecnoCoder/logout.html'), name="logout"),
    path('error', LogoutView.as_view(template_name='TecnoCoder/error.html'), name="error"),
    path('correcto', LogoutView.as_view(template_name='TecnoCoder/correcto.html'), name="correcto"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('nuevoBlog', NuevoBlog.as_view(), name = 'NuevoBlog'),
    path('update-user-profile/<int:pk>/', Update_user_profile.as_view(), name = 'update_user_profile'),
    path('editar-blog/<int:pk>/', Editar_Blog.as_view(), name = 'editar-blog'),   
    path('eliminar-blog/<int:pk>/', Delete_Blog.as_view(), name = 'eliminar-blog'),
]