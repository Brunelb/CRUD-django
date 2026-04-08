# 🛠️ Django CRUD Project – Gestion de Produits

## 📌 Description

Ce projet est une application web développée avec **Django** permettant de gérer des produits à travers les opérations CRUD (Create, Read, Update, Delete).

L’objectif est de mettre en pratique :

* la gestion des modèles Django
* les formulaires (Django Forms)
* les vues (function-based views)
* le routage (URL routing)
* les templates avec Bootstrap

---

## 🚀 Fonctionnalités

* ✅ Ajouter un produit (Create)
* ✅ Afficher la liste des produits (Read)
* ✅ Modifier un produit (Update)
* ✅ Supprimer un produit (Delete)
* ✅ Gestion des erreurs (ex: produit inexistant → page 404 personnalisée)
* ✅ Interface utilisateur avec Bootstrap

---

## 🧱 Technologies utilisées

* Python 3.x
* Django 5.x
* SQLite (base de données par défaut)
* HTML / CSS
* Bootstrap

## 🧩 Modèle principal

Exemple de modèle `Product` :

```python
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
```

---

## 🔁 CRUD – Fonctionnement

### ➕ Create

* Formulaire avec `ProductForm`
* Validation avec `form.is_valid()`
* Sauvegarde avec `form.save()`

### 📄 Read

* Liste des produits avec `Products.objects.all()`
* Affichage via boucle `{% for %}` dans les templates

### ✏️ Update

* Chargement avec `instance=obj`
* Modification puis sauvegarde

### ❌ Delete

* Confirmation avant suppression
* Redirection après suppression

---

## ⚠️ Gestion des erreurs

* Gestion manuelle avec `try/except`
* Page personnalisée pour les erreurs :

```python
except Products.DoesNotExist:
    return render(request, 'products/error404.html')
```

---

## 🎨 Interface

* Utilisation de Bootstrap pour :

  * cards produits
  * formulaires
  * boutons (create, update, delete)
* Responsive design

---

## 📌 Améliorations possibles

* 🔐 Authentification (login / register)
* 🛒 Ajout d’un panier
* 📄 Pagination des produits
* 🔍 Recherche dynamique
* 🖼️ Upload d’images produits
* 🌐 API REST avec Django REST Framework

