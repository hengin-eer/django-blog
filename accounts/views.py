from http.client import HTTPResponse
from django.shortcuts import render

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm, SignupForm

def profilepage(request):
    return render(request, 'accounts/profile.html')

# def signuppage(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)            

class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'blog/frontpage.html'