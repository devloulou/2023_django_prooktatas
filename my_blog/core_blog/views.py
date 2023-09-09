from django.shortcuts import render

from django.http import HttpResponse

from .models import PostModel
from django.contrib.auth.models import User

"""
A View fogja renderelni a HTML file-okat és odaadni a böngészőnek
"""
"""
Kezdetben function-based viewkat fogunk használni
Később class-based viewkat
"""
"""
View -> ki kell vezetni url-re ->a fő url-be behivatkozom

Tipikusan a web backend fejlesztésnél:
CRUD - Create Read Update Delete
     - Insert Select Update Delete - db utasítás
     - Post Get Put Delete - HTTP request type

"""


def index(request):
    context = {
        'posts': PostModel.objects.all() # select * from posts
    }

    # test = PostModel.objects.create(title="Manual data", content="Ez egy test", author=User.objects.get(id=1))
    # test.save()

    return render(request, 'blog/index.html', context=context)

def test_view(request):
    return HttpResponse("Test oldalon vagyok")