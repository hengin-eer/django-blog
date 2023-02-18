from django.urls import path
from accounts import views

urlpatterns = [
    path("profile/", views.profilepage, name='profile'),
    # path("signup/", name='signup'),
    path("login/", views.Login.as_view(), name='login'),
    path("logout", views.Logout.as_view(), name='logout'),
]
