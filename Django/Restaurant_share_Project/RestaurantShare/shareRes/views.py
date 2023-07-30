from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/index.html', content)

def restaurantDetail(request):
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request):
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request, 'shareRes/categoryCreate.html', content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))