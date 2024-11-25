from profiles.models import Profile
from django.shortcuts import render


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget.
# Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Vue pour afficher la liste de tous les profils.

    :param request: L'objet de la requête HTTP.
    :return: HttpResponse avec le template 'index.html'
     rendu, affichant la liste de tous les profils.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui.
# Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it.
# Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males


def profile(request, username):
    """
    Vue pour afficher les détails d'un profil spécifique.

    :param request: L'objet de la requête HTTP.
    :param username: Le nom d'utilisateur du profil à récupérer.
    :return: HttpResponse avec le template 'profile.html' rendu et les détails du profil.
    :raises Profile.DoesNotExist:
     Si aucun profil n'est trouvé pour le nom d'utilisateur fourni (erreur 404).
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
