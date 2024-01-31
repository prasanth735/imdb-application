from django.shortcuts import render,redirect

from django.views.generic import View
from myapp.models import Movie

from django import forms

# Create your views here.

class Movielistview(View):
     def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        
        return render(request,"movie_list.html",{"data":qs})


class Moviedetailview(View):
    
   def get(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       qs=Movie.objects.get(id=id)
       return render(request,"movie_detail.html",{"data":qs})
   
class Moviedeleteview(View):
   def get(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       Movie.objects.get(id=id).delete()
       return redirect("movie-list")
   

class Movieform(forms.Form):
   name=forms.CharField()
   language=forms.CharField()
   run_time=forms.IntegerField()
   genre=forms.CharField()
   director=forms.CharField()
   year=forms.IntegerField()
   actors=forms.CharField() 

class Moviecreateview(View):
    def get(self,request,*args,**kwargs):
        form=Movieform()
        return render(request,"movie_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Movieform(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Movie.objects.create(**data)
            return redirect("movie-list")
        else:
            return render(request,"movie_add.html",{"form":form})

    #     data={k:v for k,v in request.POST.items()}
    #     data.pop("csrfmiddlewaretoken")
    #     Movie.objects.create(**data)
    #     return redirect("movie-list")  


class Movieupdateview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_object=Movie.objects.get(id=id)
        data={
            "name":movie_object.name,
            "language":movie_object.language,
            "run_time":movie_object.run_time,
            "genre":movie_object.genre,
            "director":movie_object.director,
            "year":movie_object.year,
            "actors":movie_object.actors
        }
        form=Movieform(initial=data)
        return render(request,"movie_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Movieform(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Movie.objects.filter(id=id).update(**data)
            return redirect("movie-list")
        else:
            return render(request,"movie_edit.html",{"form":form})



