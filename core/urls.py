from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/login/", ObtainAuthToken.as_view()),
    path("api/v1/", include("news.urls")),
]
