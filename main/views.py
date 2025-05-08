from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def hello_view(request):
    return HttpResponse(
        """
        <h1>Hello View</h1>
        <hr>
        <p>Bu sahifa HttpResponse orqali chiqarildi!</p>
        """
    )


def home_view(request):
    return render(request, 'index.html')


def talabalar_view(request):
    talabalar = Talaba.objects.all()
    data = {
        'talabalar': talabalar,
    }
    return render(request, 'talabalar.html', context=data)

def kitoblar_view(request):
    kitoblar = Kitob.objects.order_by('nom')
    context = {
        'kitoblar': kitoblar,
    }
    return render(request, 'kitoblar.html', context)


def talaba_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba-details.html', context)


def kitobli_talabalar_view(request):
    talabalar = Talaba.objects.filter(kitob_soni__gt=0)
    data = {
        'talabalar': talabalar,
    }
    return render(request, 'kitobli-talabalar.html', data)