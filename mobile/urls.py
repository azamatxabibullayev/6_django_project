from django.urls import path
from mobile.views import get_info


urlpatterns = [
    path('mobile', get_info)
]
