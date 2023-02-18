from http.client import HTTPResponse
from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from blog.forms import PostForm
from .models import Category, Post
from django.views.generic import CreateView

def toppage(request):
    return render(request, "blog/toppage.html")

def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html", {"posts": posts})

def categorypage(request, category):
    category = Category.objects.get(name=category)
    posts = Post.objects.filter(category=category)
    return render(request, "blog/frontpage.html", {"category": category, "posts": posts})

'''special pages'''

def aboutpage(request):
    return render(request, "blog/aboutpage.html")

def contactpage(request):
    return render(request, "blog/contactpage.html")


def post_detail(request, category, slug):
    category = Category.objects.get(name=category)
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post_detail.html", {"category": category, "post": post})

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Post
    form_class = PostForm
    # success_url = reverse_lazy('frontpage')
    
    def get_success_url(self):
        messages.success(self.request, '記事を投稿しました。')
        return resolve_url('frontpage')
    
    
