from django.shortcuts import render


def index(request):
    """
    Vue pour afficher la page d'accueil du site

    :param request: requête HTTP.
    :return: HttpResponse avec le template 'index.html' rendu, affichant la page d'accueil du site
    """
    return render(request, 'index.html')
