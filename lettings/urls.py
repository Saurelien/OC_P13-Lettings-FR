from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('letting/<int:letting_id>/', views.letting, name='letting'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('lettings/', views.lettings_index, name='lettings_index'), # a remplacer par lettings/lettings_index
#     path('lettings/<int:letting_id>/', views.letting, name='letting'), # a remplacer par lettings/letting
# ]
