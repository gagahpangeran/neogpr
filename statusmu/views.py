from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Statusmu

# Create your views here.


def index(request):
    if(request.method == 'POST'):
        data = {}
        post_data = dict(request.POST.items())
        data['name'] = post_data['name']
        data['status'] = post_data['status']
        Statusmu(**data).save()

    data = {} if not Statusmu.objects.all(
    ) else {'list': Statusmu.objects.all().order_by('-date')}

    return render(request, 'landing.html', data)
