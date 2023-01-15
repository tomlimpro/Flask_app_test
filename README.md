
#  Flask app MEMO

## Requirements
* Flask==2.2.2
* Jinja2==3.1.2
* markupsafe==2.1.1
* itsdangerous==2.1.2
* werkzeug==2.2.2

### Flask

Flask est un cadre web open-source pour le développement d'applications en python. Il est conçu pour être léger et facile à utiliser. Simple et flexible.

Permet de définir des routes pour les URL et de les mapper à des fonctions de traitement de requêtes qui gèrent les données et les logiques de l'application.

### Jinja

Jinja est un moteur de template pour le langage de programmation python.
Il est utilisé pour générer des pages web dynamiques en combiannt des données de modèle avec un template.
Jinja est utilisé avec Flask.

On peut créer des templates HTML qui contiennent des variables et des instructions de boucles et de conditions, qui sont remplacées
par des données lorque le template est rendu. Cela permet de séparer les données de la présentation, facilitant la maintenant et la modification de l'application.

Il offre une série d'outils pour manipuler les données, comme des filtres et des fonctions de test, qui permettent de formater les données pour l'affichage ou de vérifier si elles répondent à certaines conditions.

#### Cheatsheet

**Basic**
* Afficher la valeur x 
```python
{{ x }}

```
* Expression 
```python
{{ x + 1}}

```

**Control structures**
```python
{% for x in range(5) %}
    {% if x % 2 == 0 %}
        {{ x }} is even!
    {% else %}
        {{ x }} is odd!
    {% endif %}
{% endfor %}

```

**Special block**
```python
{% filter e %}
{% raw %}
    This is a raw block where {{nothing is evaluated}}
    {% not even this %}
    and <html is escaped> too with "e" filter
{% endraw %}
{% endfilter %}

{% macro myfunc(x) %}
    this is a reusable macro, with arguments: {{x}}
{% endmacro %}

{{ myfunc(42) }}

{#
this is a comment
#}

```

### itsdangerous

itsdangerous est un module Python pour aider à générer et à vérifier des jetons de sécurité pour les applications web.
Il est souvent utilisé pour générer des jetons d'authentification ou des jetons de session pour les users connectés. Il est également utilisé pour signer des données sensibles pour les protéger contre la modification non autorisée.

Il utilise des algo de hachage cryptographique pour signer des données de manière sécurisée. 

### werkzeug

Werkzeug est un kit d'outils pour le développement web en Python. Il est utilisé pour créer des serveurs web et des applications web.
Il est également utilisé comme utilitaire pour exécuter des scripts et des commandes en ligne.

Les fonctionnalités incluent : 

* Un serveur web de développement intégré qui peut être utilisé pour tester des applications web en cours de dev.
* Un utilitaire pour exécuter des scripts en ligne.
* Une bibliothèque URL routing qui permet de mapper des URL à des fonctions de traitement de requêtes.
* Une bibliothèque de requêtes et de réponses HTTP qui peut être utilisée pour créer et manipuler des objets de requêtes et de réponses HTTP.