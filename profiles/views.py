from profiles.models import Profile
from django.shortcuts import render


def index(request):
    """
    Vue pour afficher la liste de tous les profils.

    :param request: L'objet de la requête HTTP.
    :return: HttpResponse avec le template 'index.html' rendu, affichant la liste de tous les profils.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Vue pour afficher les détails d'un profil spécifique.

    :param request: L'objet de la requête HTTP.
    :param username: Le nom d'utilisateur du profil à récupérer.
    :return: HttpResponse avec le template 'profile.html' rendu et les détails du profil.
    :raises Profile.DoesNotExist: Si aucun profil n'est trouvé pour le nom d'utilisateur fourni (erreur 404).
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
