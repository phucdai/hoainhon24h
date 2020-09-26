from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse
import requests
# Create your views here.

def Weather(request):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Quy nhon&appid=c15b2c26b7d5d0028868fb0d2de8a80c')
    reponsedata = r.json()
    main = reponsedata['main']
    temp = main['temp'] - 273
    temp_max = main['temp_max'] - 273
    temp_min = main['temp_min'] - 273
    city = reponsedata['name']
    weather = reponsedata['weather'][0]
    icon = weather['icon']
    data = {
        'temp': temp,
        'temp_max': int(temp_max),
        'temp_min': int(temp_min),
        'city': city,
        'icon': icon,
    }
    return data


class Home(View):
    def get(self, request):
        data = {
            'post_list' : Post.objects.filter(status=1).order_by('-created_on'),
            'trends': Post.objects.filter(status=1).order_by('-hits'),
            'hoainhon': Post.objects.filter(status=1, category=1).order_by('-created_on'),
            'thoisu': Post.objects.filter(status=1, category=2).order_by('-created_on'),
            'amthuc': Post.objects.filter(status=1, category=3).order_by('-created_on'),
            'thethao': Post.objects.filter(status=1, category=4).order_by('-created_on'),
            'doisong': Post.objects.filter(status=1, category=5).order_by('-created_on'),
            'giaitri': Post.objects.filter(status=1, category=6).order_by('-created_on'),
            'tuyendung': Post.objects.filter(status=1, category=7).order_by('-created_on'),
        }
        return render(self.request, 'core/index.html', data)


class View(View):
    def get(self, request, slug):
        h = Post.objects.get(slug=slug)
        category = h.category
        data = {
            'trends' : Post.objects.filter(status=1).order_by('-hits'),
            'news' : Post.objects.filter(status=1).order_by('-created_on'),
            'post' : Post.objects.get(slug=slug),
            'tinlienquan': Post.objects.filter(status=1, category=category).order_by('-created_on'),
        }
        h.hits += 1
        h.save()
        return render(self.request, 'core/detail.html', data)


class Categories(View):
    def get(self, request, slug):
        d = Category.objects.get(slug=slug)
        id = d.id
        data = {
            'post_list': Post.objects.filter(category=id, status=1).order_by('-created_on'),
            'title': d,
            'trends': Post.objects.filter(status=1).order_by('-hits'),
            'news': Post.objects.filter(status=1).order_by('-created_on'),
        }
        return render(self.request, 'core/category.html', data)