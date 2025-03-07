=======================
Guide d'Utilisation
=======================

Prérequis
=========
---- TOTO -----
Avant de commencer à utiliser l'application, assurez-vous d'avoir :

1. **Environnement requis** : Python 3.x et **Django 3.0**.
2. **Base de données** : SQLite est utilisée par défaut pour stocker les données.

Fonctionnalités Principales
==========================

1. **Gestion des adresses** : Permet de créer et gérer les adresses liées aux locations.
2. **Gestion des locations** : Permet de créer, afficher et gérer les locations.
3. **Gestion des profils** : Permet aux utilisateurs de gérer leurs informations personnelles et de définir une ville préférée.

---

1. **Gestion des Adresses**
===========================

Une adresse est associée à chaque location.

Attributs d'une adresse :
-------------------------
- **number** : Numéro de rue (maximum 9999).
- **street** : Nom de la rue (maximum 64 caractères).
- **city** : Ville (maximum 64 caractères).
- **state** : État (2 caractères, ex : NY).
- **zip_code** : Code postal (maximum 99999).
- **country_iso_code** : Code pays ISO (3 caractères, par exemple : USA).

Cas d'Utilisation :
------------------
- **Créer une nouvelle adresse** :
   1. Accédez à l'interface d'administration sous `Addresses`.
   2. Cliquez sur **Ajouter**.
   3. Remplissez les informations et cliquez sur **Enregistrer**.

---

2. **Gestion des Locations (Lettings)**
=====================================

Une location est associée à une adresse.

Attributs d'une location :
--------------------------
- **title** : Titre de la location (ex : "Maison au bord de la mer").
- **address** : Adresse associée (relation One-to-One avec `Address`).

Cas d'Utilisation :
------------------
- **Créer une nouvelle location** :
   1. Accédez à l'interface d'administration sous `Lettings`.
   2. Cliquez sur **Ajouter**.
   3. Associez une adresse et ajoutez un titre.
   4. Cliquez sur **Enregistrer**.

- **Afficher toutes les locations** :
   1. Allez à la page `/lettings/` pour voir la liste des locations.
   2. Cliquez sur une location pour voir ses détails.

---

3. **Gestion des Profils Utilisateurs**
====================================

Chaque utilisateur est associé à un profil via une relation *One-to-One*.

Attributs d'un profil :
----------------------
- **user** : L’utilisateur associé (relation One-to-One avec `User`).
- **favorite_city** : Ville préférée de l’utilisateur.

Cas d'Utilisation :
------------------
- **Créer un profil utilisateur** :
   1. Accédez à l'interface d'administration sous `Profiles`.
   2. Cliquez sur **Ajouter un profil**.
   3. Sélectionnez un utilisateur existant et ajoutez une ville préférée.
   4. Cliquez sur **Enregistrer**.

- **Afficher le profil d'un utilisateur** :
   1. Accédez à la page `/profiles/`.
   2. Recherchez un utilisateur et cliquez sur son nom pour voir les détails de son profil.

---

Cas d'Utilisation Détaillés
==========================

**Cas 1 : Ajouter une location avec une nouvelle adresse**
---------------------------------------------------------
1. Connectez-vous à l’interface d’administration.
2. Créez une nouvelle adresse sous `Addresses`.
3. Créez une nouvelle location sous `Lettings`, associez l'adresse nouvellement créée.
4. Donnez un titre à la location et enregistrez.

**Cas 2 : Associer une ville préférée à un utilisateur**
--------------------------------------------------------
1. Accédez à l’interface d’administration, section `Profiles`.
2. Cliquez sur **Ajouter un profil**.
3. Sélectionnez un utilisateur et ajoutez une ville préférée.
4. Cliquez sur **Enregistrer**.

**Cas 3 : Afficher toutes les locations disponibles**
------------------------------------------------------
1. Accédez à la page `/lettings/` et consultez la liste des locations.
2. Cliquez sur une location pour afficher les détails.

**Cas 4 : Rechercher les utilisateurs ayant une ville préférée commençant par "B"**
------------------------------------------------------------------------------------
1. Ouvrez une session sqlite3 sous powershell :
 - Ouvrez la db:
  - .open oc-lettings-site.sqlite3
2. Afficher les colonnes de la db:
 - .tables
3. Afficher les informations des profiles:
 - pragma table_info(profiles_profile);
4. Afficher les villes favorite commencant par B:
 - select user_id, favorite_city from profiles_profile where favorite_city like 'B%';

-------

**Le résultat devrait ressembler à ceci:**
---------------------------------------------

 - Use ".open FILENAME" to reopen on a persistent database.
  - sqlite> .open oc-lettings-site.sqlite3
 - sqlite> .tables
  - auth_group                  django_content_type
  - auth_group_permissions      django_migrations
  - auth_permission             django_session
  - auth_user                   lettings_address
  - auth_user_groups            lettings_letting
  - auth_user_user_permissions  profiles_profile
  - django_admin_log
 - sqlite> pragma table_info(profiles_profile);
  - 0|id|INTEGER|1||1
  - 1|favorite_city|varchar(64)|1||0
  - 2|user_id|INTEGER|1||0
 - sqlite> select user_id, favorite_city from profiles_profile where favorite_city like 'B%';
  - 5|Buenos Aires
  - 4|Barcelona
  - 3|Budapest
  - 2|Berlin


