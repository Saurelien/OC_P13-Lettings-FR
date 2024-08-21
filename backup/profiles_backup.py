from django.db import migrations


def forwards_func(apps, schema_editor):
    Profile = apps.get_model("profiles", "Profile")
    ProfileLegacy = apps.get_model("oc_lettings_site", "Profile")

    # for letting in LettingLegacy.objects.all():
    #     Letting.objects.create(title=letting.title, adress=letting.adress)
    profiles = []
    for profile in ProfileLegacy.objects.all():
        profiles.append(Profile(user=profile.user, favorite_city=profile.favorite_city))
    Profile.objects.bulk_create(profiles)


def reverse_func(apps, schema_editor):
    Profile = apps.get_model("profiles", "Profile")

    Profile.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
