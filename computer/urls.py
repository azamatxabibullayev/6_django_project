from django.urls import path
from computer.views import computer


urlpatterns = [
    path('computer', computer)
]
