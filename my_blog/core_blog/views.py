from django.shortcuts import render

from django.http import HttpResponse

from .models import PostModel
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

# csak get request
def index(request):
    context = {
        'posts': PostModel.objects.all().order_by('-date_posted') # select * from posts
    }

    return render(request, 'blog/index.html', context=context)

## index function based view  - Class Based View-t
class PostsListView(ListView):
    model = PostModel
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog/post_detail.html'

def post_detail_view(request, pk):
    if request.method == 'POST':
        return HttpResponse('Wrong request type')
    
    context = {
        'object': PostModel.objects.get(id=pk)
    }
    return render(request, 'blog/post_detail.html', context=context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostModel
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        # beégetjük, hogy minden user az admin legyen
        # itt kellene lekérni az admin user-t
        form.instance.author = self.request.user
        return super().form_valid(form)

def about_view(request):
    return render(request, 'blog/about.html')

def test_view(request):
    return HttpResponse("Test oldalon vagyok")


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostModel
    template_name = 'blog/post_delete.html'
    success_url = '/' #kezedő oldal

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostModel
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False