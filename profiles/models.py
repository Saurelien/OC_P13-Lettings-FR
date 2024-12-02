from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente un profil utilisateur.

    Attributs :
        user (User) : Chaque utilisateur a un profil unique, relation OneToOneField ( User django )
        favorite_city (str) : Ville préférée de l'utilisateur. Champs personnalisé pour l'utilisateur permettant
         a ce dernier de specifier sa ville favorite.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Représentation textuelle d'un profil.

        Return :
            str : Le nom d'utilisateur associé au profil.
        """
        return self.user.username
