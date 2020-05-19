from django.urls import path
from Audio import views

urlpatterns = [
    path("", views.index)
]
