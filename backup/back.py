from django.db import migrations


def forwards_func(apps, schema_editor):
    Letting = apps.get_model("lettings", "Letting")
    LettingLegacy = apps.get_model("oc_lettings_site", "Letting")

    Address = apps.get_model("lettings", "Address")
    AddressLegacy = apps.get_model("oc_lettings_site", "Address")
    # for letting in LettingLegacy.objects.all():
    #     Letting.objects.create(title=letting.title, adress=letting.address)
    adresses = []
    for address in AddressLegacy.objects.all():
        adresses.append(Address(
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            country_iso_code=address.country_iso_code
        ))
    Address.objects.bulk_create(adresses)

    lettings = []
    for letting in LettingLegacy.objects.all():
        lettings.append(Letting(
            title=letting.title,
            address=letting.address
        ))
    Letting.objects.bulk_create(lettings)


def reverse_func(apps, schema_editor):
    Letting = apps.get_model("lettings", "Letting")

    Letting.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
