from django.contrib import admin
from django.urls import path, include
from services.error_handler import custom_404_view, custom_500_view
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('404', custom_404_view, name='404'),
    path('500', custom_500_view, name='500'),
    path('sentry-debug/', views.trigger_sentry_error, name='sentry_debug')
]

handler404 = custom_404_view
handler500 = custom_500_view
