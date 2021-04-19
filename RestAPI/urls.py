from RestAPI.views import *
from django.urls import path

urlpatterns = [
    path("makanan/",makananList.as_view()),
    path("makanan/<int:pk>/",makananDetail.as_view()),
]