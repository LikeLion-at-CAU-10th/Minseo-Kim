from importlib.resources import path
from django.urls import path
from .views import *

urlpatterns = [
    path('create-profile/', create_profile, name="create-profile" ),
    path('get-profile-all/', get_profile_all, name= 'get-profile-all'),
    path('get-profile/<int:id>', get_profile, name= 'get-profile'),
]