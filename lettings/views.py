from django.http import Http404
from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    Vue pour afficher la page d'accueil du site

    :param request: requête HTTP.
    :return: HttpResponse avec le template 'index.html' rendu, affichant la page d'accueil des locations
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une location spécifique.

    :param request: L'objet de la requête HTTP.
    :param letting_id: L'identifiant unique de la location à récupérer.
    :return: HttpResponse avec le template 'letting.html' rendu et les détails de la location.
    :raises Letting.DoesNotExist: Si aucune location n'est trouvée avec l'ID fourni (erreur 404).
    """
    try:
        if not letting_id == 999999999:
            raise ValueError("Test afin de déclencher une erreur 500")

        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)

    except Letting.DoesNotExist:
        raise Http404("La location demandée n'existe pas.")

    except ValueError as e:
        raise Exception("Une erreur interne s'est produite: " + str(e))

