from multiprocessing import context
from pickle import EMPTY_TUPLE
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from TecnoCoder.models import Avatar, Blog
from TecnoCoder.forms import   UserRegisterForm, UserRegisterForm,UserEditForm
from django.contrib.auth.forms import UserChangeForm
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView, UpdateView, DeleteView
      
def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id).exists()
      
      if  request.user.is_authenticated and avatares == True:
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request, "TecnoCoder/inicio.html", {"url": avatares[0].imagen.url})
            
      else: 
            avatares = False   
            return render(request, "TecnoCoder/inicio.html", {'avatar': avatares})
      
      
def nosotros(request):
      avatares = Avatar.objects.filter(user=request.user.id).exists()
      if  request.user.is_authenticated and avatares == True :
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request, "TecnoCoder/nosotros.html", {"url": avatares[0].imagen.url})            
      else:
            return render(request, "TecnoCoder/nosotros.html")

@login_required
def blog(request):
      blog = Blog.objects.all()
      avatares = Avatar.objects.filter(user=request.user.id).exists()
      
      if  request.user.is_authenticated and avatares == True:
            
            blog = Blog.objects.all()
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request, "TecnoCoder/blog.html", {"url": avatares[0].imagen.url,'blog': blog})
      else:
            
            return render(request, "TecnoCoder/blog.html", {'blog': blog})
      

def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  
                  user = authenticate(username=usuario, password = contra)
                  
                  
                  if user is not None:
                        login(request, user)
                        avatares = Avatar.objects.filter(user=request.user.id).exists()
                        if avatares == True:
                              avatares = Avatar.objects.filter(user=request.user.id)
                              print(avatares)
                              return render(request, "TecnoCoder/inicio.html", {"url": avatares[0].imagen.url})
                        #return render(request, "TecnoCoder/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                        else:
                              return render(request, "TecnoCoder/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        return render(request, "TecnoCoder/error.html", {"mensaje": f"Error, datos incorrectos"})
            
            else:
                  return render(request,"TecnoCoder/error.html", {"mensaje": f"Error, formulario equivocado"})      
      
      form = AuthenticationForm()
      return render(request, "TecnoCoder/login.html", {"form": form})        

def register(request):
      form = UserRegisterForm(request.POST)
      if form.is_valid():
            
            username = form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            
            form.save()
            return render(request, "TecnoCoder/correcto.html", {"mensaje":"Usuario Creado!"})
      
      else:
            form = UserRegisterForm()
      
      return render(request, "TecnoCoder/registro.html", {"form": form})      

@login_required
def editarPerfil(request):
      usuario = request.user
      avatares = Avatar.objects.filter(user=request.user.id)
      imagen =avatares[0].imagen.url
      idImagen = avatares[0].id
      print(idImagen)
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid:
                  
                  informacion = miFormulario.data
                  
                  usuario.first_name = informacion['first_name']
                  usuario.email= informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
                  
                  return render (request, "TecnoCoder/inicio.html")
      
      else:      
            
            miFormulario = UserEditForm(initial={ 'fist_name': usuario.first_name, 'email':usuario.email})
      
      return render(request, 'TecnoCoder/editarPerfil.html', {'miFormulario':miFormulario, 'usuario':usuario,'imagen':imagen,'id':idImagen})     

class Update_user_profile(LoginRequiredMixin,UpdateView):
    model = Avatar
    template_name = 'TecnoCoder/editarFoto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('Blog')

class Editar_Blog(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = 'TecnoCoder/editarBlog.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('Blog')

class NuevoBlog(LoginRequiredMixin,CreateView):
      model = Blog
      template_name = 'TecnoCoder/create_blog.html'
      fields = '__all__'
      
      def get_success_url(self):
        return reverse('Blog')


class Delete_Blog(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'TecnoCoder/delete_blog.html'

    def get_success_url(self):
        return reverse('Blog')


