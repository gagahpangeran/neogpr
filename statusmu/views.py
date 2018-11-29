from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Statusmu, User
from django.contrib.auth import logout
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
        data['desc'] = "" if 'description' not in info['volumeInfo'] else info['volumeInfo']['description'][:300]
        data['author'] = "" if 'author' not in info['volumeInfo'] else ", ".join(
            info['volumeInfo']['authors'])
        data['image'] = info['volumeInfo']['imageLinks']['thumbnail']
        data['preview'] = info['volumeInfo']['previewLink']
        items.append(data)

    return JsonResponse({"data": items})


def register(request):
    return render(request, 'register.html')


def check_email(request):
    exist = False
    if(request.body):
        data = json.loads(request.body)
        exist = User.objects.filter(email=data['email']).exists()

    return JsonResponse({"exist": exist})


def reg(request):
    success = False
    if(request.body):
        data = json.loads(request.body)
        try:
            User(**data).save()
            success = True
        except:
            success = False

    return JsonResponse({"success": success})


def subscriber(request):
    data = list(reversed(list(User.objects.values())))

    return JsonResponse({"data": data})


def delete_subs(request):
    success = False
    if(request.body):
        data = json.loads(request.body)
        User.objects.filter(id=data['id']).delete()
        success = True

    return JsonResponse({"success": success})

def log_out(request):
    logout(request)
    return redirect('index')
