from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('letting/<int:letting_id>/', views.letting, name='letting'),
]
