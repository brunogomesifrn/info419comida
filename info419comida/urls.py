"""info419comida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core.views import registro, dados, tipo, index, dados, receitax, cadastrar_receita, cadastrar_tipo, perfil 

urlpatterns = [
    
    path('perfil/', perfil, name='perfil'),
    path('cadastrar_tipo/', cadastrar_tipo, name='cadastrar_tipo'), 
    path('cadastrar_receita/', cadastrar_receita, name='cadastrar_receita'),
    path('receita/', receitax, name='receita'),
    path('dados/<int:id>/', dados, name='dados'),
    path('', index, name='index'),    
    path('tipo/', tipo, name='tipo'),   
    path('dados/<int:id>/', dados, name='dados'),
    path('registro/', registro, name='registro'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
