from django.shortcuts import render
from .models import Noticia
from django import forms

def index(request):
    return render(request,"noticias/index.html")

def noticias_lista(request):
    noticias = Noticia.objects.all()
    return render(request,'noticias/lista.html',{'noticias':noticias})

class NewsSearchForm(forms.Form):
  query = forms.CharField()  

def news_search(request):
   
    if request.method == 'GET':
        form = NewsSearchForm(request.GET)
        print(request.GET)

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Noticia.objects.filter(title__icontains=query) | Noticia.objects.filter(content__icontains=query)
        form = NewsSearchForm()
        return render(request, 'noticias/busqueda.html', {'results': results, 'buscada': query,'form': form})
    else:
        form = NewsSearchForm()

    return render(request, 'noticias/busqueda.html', {'form': form})