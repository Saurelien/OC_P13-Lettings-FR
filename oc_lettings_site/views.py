from django.shortcuts import render
from django.http import HttpResponse


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Vue pour afficher la page d'accueil du site

    :param request: requête HTTP.
    :return: HttpResponse avec le template 'index.html' rendu, affichant la page d'accueil du site
    """
    return render(request, 'index.html')


def trigger_sentry_error(request):
    if request.user and request.user.is_authenticated and request.user.is_staff:
        raise Exception("Erreur intentionnelle pour la journalisation sentry")
    return HttpResponse()
