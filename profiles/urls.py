from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('profiles/', views.profiles_index, name='profiles_index'),# a remplacer par profiles/profiles_index
#     path('profiles/<str:username>/', views.profile, name='profile'),# a remplacer par profiles/profile
# ]
