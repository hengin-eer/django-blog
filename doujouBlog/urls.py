from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from blog import views

from blog.views import aboutpage, categorypage, contactpage, frontpage, post_detail, toppage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", toppage),
    path("blog", frontpage, name="frontpage"),
    path("category/<str:category>/", categorypage, name="category"),
    path("about/", aboutpage),
    path("contact/", contactpage),
    path("blog/<str:category>/<slug:slug>/", post_detail, name="post_detail"),
    path("create", views.PostCreateView.as_view(), name="post_create"),
    # accounts
    path("accounts/", include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)