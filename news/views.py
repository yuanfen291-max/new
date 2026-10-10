from django.shortcuts import render
from news.models import NewsModel
from django.views.generic import ListView

class NewsList(ListView):
    model = NewsModel
    template_name = 'index.html'