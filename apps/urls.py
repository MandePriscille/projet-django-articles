from django.urls import path
from apps.views import get

urlpatterns = [
   path('',get)
]