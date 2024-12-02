=====================
Guide de Déploiement
=====================

Ce guide explique comment fonctionne le pipeline CI/CD configuré pour ce projet.

Structure du Pipeline CI/CD
===========================

Le pipeline est divisé en trois étapes principales : **test**, **build** et **deploy**. Voici un aperçu de chaque étape.

1. **Déclenchement**
 - Le pipeline s'exécute automatiquement dans les cas suivants :
     - Lorsqu'une modification est poussée sur les branches `develop` ou `master`.
     - Lorsqu'une pull request est ouverte vers la branche `develop`.

Étape 1 : Tests
================

1. **Mise en place de l'environnement**
    - Télécharge le code source depuis le dépôt GitHub.
    - Installe Python 3.11 et crée un environnement virtuel.
    - Installe les dépendances nécessaires (spécifiées dans `requirements.txt`) et `coverage` pour mesurer la couverture des tests.

2. **Exécution des tests**
    - Lance les tests unitaires à l'aide de `coverage`.
    - Génère un rapport de couverture avec un minimum de 80%

3. **Archiver le rapport de couverture**
    - Le rapport HTML généré est sauvegardé comme artefact ( possible de le télécharger )

Étape 2 : Build (Construction de l'image Docker)
=================================================

Si les tests réussissent sur la branche `master`, le pipeline passe à la construction de l'image Docker.

1. **Préparation de l'environnement Docker**
    - Configure Docker Buildx pour la construction de l'image.
    - Connecte le pipeline à Docker Hub en utilisant les informations d'identification stockées dans les secrets GitHub Action.

2. **Construction de l'image Docker**
    - Construit une image Docker à partir du fichier `Dockerfile` de l'application.

3. **Tag et Push**
 - L'image Docker est étiquetée avec deux tags :
     - `latest` : pour identifier la version la plus récente.
     - Un tag unique basé sur le hash du commit (ex. : `sha`), pour un suivit du versioning.
     - Les deux tags sont ensuite poussés sur Docker Hub.

Étape 3 : Déploiement sur Render
================================

Si la construction de l'image est réussie, le pipeline déploie automatiquement l'application sur la plateforme Render.

1. **Préparation des variables**
    - L'image Docker à déployer est identifiée grâce au tag `latest`.
    - Les informations nécessaires au déploiement (ID du service Render et clé API) sont récupérées à partir des secrets GitHub Action.

2. **Déploiement**
    - Utilise une requête API pour notifier Render qu'une nouvelle version de l'image Docker est disponible.
    - Render déploie alors automatiquement cette image pour mettre à jour l'application.

Comment personnaliser ?
========================

Vous pouvez ajuster le pipeline selon vos besoins :

- **Ajouter des branches au déploiement** : Modifiez la section `on: push` pour inclure d'autres branches.
- **Modifier l'environnement** : Mettez à jour les variables d'environnement ou secrets dans les paramètres GitHub.
- **Étendre les tests** : Ajoutez des étapes pour d'autres types de tests ou de vérifications (linting, tests d'intégration, etc.).

Résumé des secrets nécessaires
==============================

Voici une liste des secrets GitHub Action utilisés dans ce pipeline et leur rôle :

- **SECRET_KEY** : La clé Django utilisée lors des tests.
- **DOCKERHUB_USERNAME** et **DOCKERHUB_TOKEN** : Identifiants pour accéder au Docker Hub.
- **RENDER_SERVICE_ID** : Identifiant unique du service Render.
- **RENDER_API_KEY** : Clé API pour interagir avec Render.

---

