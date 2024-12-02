from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Représente une adresse physique.

    Attributs :
        number (int) : Le numéro de la rue. Inférieur ou égal à 9999.
        street (str) : Le nom de la rue. Maximum de 64 caractères.
        city (str) : Le nom de la ville. Maximum de 64 caractères.
        state (str) : Abréviation de l'état où se situe l'adresse. Par exemple "NY" ou "NC".
        zip_code (int) : Le code postal. Inférieur ou égal à 99999.
        country_iso_code (str) : Le code ISO du pays en l'occurence "USA".
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
        Métadonnées pour le modèle Address.
        """
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Représentation textuelle d'une adresse.

        return :
            str : Une chaîne de caractère contenant le numero et le nom de la rue".
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Représente une location associée à une adresse.

    Attributs :
        title (str) : Titre ou Nom de la location. Longueur maximale de 256 caractères.
        address (Address) : Une relation One-to-One avec le modèle Address.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='letting')

    def __str__(self):
        """
        Représentation textuelle d'une location.

        Return :
            str : Le titre ou Nom de la location.
        """
        return self.title
