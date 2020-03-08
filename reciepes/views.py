from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe


def index(request):
    re = Recipe.objects.all()
    context = {'recipe': re}
    return render(request, 'reciepes/index.html', context)


def detail(request, id):
    check = get_object_or_404(Recipe, pk=id)
    return render(request, 'reciepes/detail.html',{'check': check})


