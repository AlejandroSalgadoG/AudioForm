from django.urls import path
from Audio import views

urlpatterns = [
    path("", views.Index.as_view())
]
