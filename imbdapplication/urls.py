"""
URL configuration for imbdapplication project.

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("movie/all/",views.Movielistview.as_view(),name="movie-list"),
    path("movie/<int:pk>/",views.Moviedetailview.as_view(),name="movie-detail"),
    path("movie/<int:pk>/remove/",views.Moviedeleteview.as_view(),name="movie-remove"),
    path("movie/add/",views.Moviecreateview.as_view(),name="movie-add"),
    path("movie/<int:pk>/change/",views.Movieupdateview.as_view(),name="movie-edit")

]
