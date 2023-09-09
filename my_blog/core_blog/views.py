from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
"""
A View fogja renderelni a HTML file-okat és odaadni a böngészőnek
"""
"""
Kezdetben function-based viewkat fogunk használni
Később class-based viewkat
"""
"""
View -> ki kell vezetni url-re ->a fő url-be behivatkozom
"""


def index(request):
    return HttpResponse("Üdv a Django kurzuson")

def test_view(request):
    return HttpResponse("Test oldalon vagyok")