from django.shortcuts import render
from .models import New
from django.views.generic.base import View
# Create your views here.
class ViewNews(View):
    news = New.objects.all()
    return render(request,'main.html',{'news_list': news})