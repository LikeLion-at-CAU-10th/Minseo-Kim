from importlib.resources import path
from django.urls import path
from .views import *

urlpatterns = [
    path('create-profile/', create_profile, name="create-profile" ),
    path('get-profile-all/', get_profile_all, name= 'get-profile-all'),
    path('get-profile/<int:id>', get_profile, name= 'get-profile'),

    path('create-url/<int:profile_id>', create_url, name="create-url"),
    path('get-url-all/<int:profile_id>', get_url_all, name="get-url-all"),
]