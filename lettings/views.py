from django.http import Http404
from django.shortcuts import render
from lettings.models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa.
# Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
# cubilia curae; Cras eget scelerisque
def index(request):
    """
    Vue pour afficher la page d'accueil du site

    :param request: requête HTTP.
    :return: HttpResponse avec le template 'index.html'
     rendu, affichant la page d'accueil des locations
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)

# Cras ultricies dignissim purus,
# vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend.
# Praesent dignissim,odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus.
# Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna.
# Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero,
# eget bibendum lorem.
# Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.


def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une location spécifique.

    :param request: L'objet de la requête HTTP.
    :param letting_id: L'identifiant unique de la location à récupérer.
    :return: HttpResponse avec le template 'letting.html' rendu et les détails de la location.
    :raises Letting.DoesNotExist: Si aucune location n'est trouvée avec l'ID fourni (erreur 404).
    """
    try:
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
