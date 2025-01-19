from django.urls import path
from .views import index, sign

urlpatterns = [
    path("", index, name="home"),
    path("sign/", sign, name="sign")
]