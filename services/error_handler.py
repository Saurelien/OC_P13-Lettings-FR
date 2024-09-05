from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def custom_404_view(request, exception=None):
    return HttpResponseNotFound(render(request, '404.html'))


def custom_500_view(request, exception=None):
    return HttpResponseServerError(render(request, '500.html'))
