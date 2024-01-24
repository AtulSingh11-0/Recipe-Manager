"""
URL configuration for first_app project.

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
from demo.views import *
from Recipe.views import *
from first_app import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    
    # routes for demo project
    path('', index, name="index"),
    path('users/', userData, name="userData"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    
    # routes for Recipe project
    path('recipe/', recipeForm, name='recipeForm'),
    path('recipes/', recipes, name='recipes'),
    path('recipeDelete/<id>/', deleteRecipe, name='deleteRecipe'),
    path('recipeUpdate/<id>/', updateRecipe, name='updateRecipe'),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
urlpatterns += staticfiles_urlpatterns()