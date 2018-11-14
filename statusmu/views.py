from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Statusmu
import requests
import json

# Create your views here.


def index(request):
    if(request.method == 'POST'):
        data = {}
        post_data = dict(request.POST.items())
        data['name'] = 'Anonim' if post_data['name'] == '' else post_data['name']
        data['status'] = post_data['status']
        Statusmu(**data).save()

    data = {} if not Statusmu.objects.all(
    ) else {'list': Statusmu.objects.all().order_by('-date')}

    return render(request, 'landing.html', data)


def profile(request):
    return render(request, 'profile.html')


def books(requests):
    return render(requests, 'books.html')


def data_book(request):
    raw_data = requests.get(
        'https://www.googleapis.com/books/v1/volumes?q=quilting').json()

    items = []
    for info in raw_data['items']:
        data = {}
        data['id'] = info['id']
        data['title'] = info['volumeInfo']['title']
        data['desc'] = info['volumeInfo']['description'][:300]
        data['author'] = ", ".join(info['volumeInfo']['authors'])
        data['image'] = info['volumeInfo']['imageLinks']['thumbnail']
        data['preview'] = info['volumeInfo']['previewLink']
        items.append(data)

    return JsonResponse({"data": items})
