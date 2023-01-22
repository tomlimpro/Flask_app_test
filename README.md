
#  Flask app MEMO

Voici la liste des sections :



# MEMO FLASK APP

## Requirements
* Flask==2.2.2
* Jinja2==3.1.2
* markupsafe==2.1.1
* itsdangerous==2.1.2
* werkzeug==2.2.2

### Flask

Flask est un cadre web open-source pour le développement d'applications en python. Il est conçu pour être léger et facile à utiliser. Simple et flexible.

Permet de définir des routes pour les URL et de les mapper à des fonctions de traitement de requêtes qui gèrent les données et les logiques de l'application.

#### Cheatsheet

`url_for()` est une fonction utilisée pour générer des URLs pour les routes définies dans une application. Elle prend en entrée le nom de la fonction 
de la route et peut éggalement prendre en entrée des arguments pour les paramètres de la route. Elle retourne une chaîne contenant l'URL générée.

Exemple : 
```python
@app.route('/user/<username>')
def user_profile(username):
    pass

```
On peut générer l'URL pour cette route en utilisant `url_for()`

```python
url = url_for('user_profile', username='johndoe')
```
La variable `url` contiendra "`/user/johndoe`"

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


# MEMO MONGODB
 - [MongoDB cheatsheet](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/)

Dans le conteneur MongoDB, il faut insérer cette commande pour se connectec à la database
```
mongo
```
permet de sauvegarder les données d'une base de données MongoDB en utilisant un format BSON
```
mongodump
```
permet de restaurer les données d'une sauvegarde MongoDB en utilisant un format BSON.
```
mongorestore
```
permet de surveiller les performances de votre base de données MongoDB en temps réel.
```
mongostat
```
permet de exporter les données de la base de données MongoDB dans un format JSON, CSV ou TSV.
```
mongoexport
```
permet d'importer les données dans une base de données MongoDB à partir d'un fichier JSON, CSV ou TSV
```
mongoimport
```
## Helpers

**Show Databases**
```
show dbs
db // prints the current database
```
**Switch Databases**
```
use <database_name>
```
**Show Collections**
```
show collections
```
**Run Javascript File**
```
load("myScripts.js")
```

## CRUD
**Create**
```
db.coll.insertOne({name: "Max"})
db.coll.insert([{name: "Max"},{name:"Alex"}])
db.coll.insert([{name: "Max"},{name:"Alex"}], {ordered: false})
db.coll.insert({date: ISODate()})
db.coll.insert({name:"Max"},{"writeConcern":{"w":"Majority,"wtimeout":5000}})
```

**Read**
```
db.coll.findOne() // returns a single document
db.coll.find()    // returns a cursor - show 20 results - "it" to display more
db.coll.find().pretty()
db.coll.find({name: "Max", age: 32}) // implicit logical "AND".
db.coll.find({date: ISODate("2020-09-25T13:57:17.180Z")})
db.coll.find({name: "Max", age: 32}).explain("executionStats") // or "queryPlanner" or "allPlansExecution"
db.coll.distinct("name")

// Count
db.coll.count({age: 32})          // estimation based on collection metadata
db.coll.estimatedDocumentCount()  // estimation based on collection metadata
db.coll.countDocuments({age: 32}) // alias for an aggregation pipeline - accurate count

// Comparison
db.coll.find({"year": {$gt: 1970}})
db.coll.find({"year": {$gte: 1970}})
db.coll.find({"year": {$lt: 1970}})
db.coll.find({"year": {$lte: 1970}})
db.coll.find({"year": {$ne: 1970}})
db.coll.find({"year": {$in: [1958, 1959]}})
db.coll.find({"year": {$nin: [1958, 1959]}})

// Logical
db.coll.find({name:{$not: {$eq: "Max"}}})
db.coll.find({$or: [{"year" : 1958}, {"year" : 1959}]})
db.coll.find({$nor: [{price: 1.99}, {sale: true}]})
db.coll.find({
  $and: [
    {$or: [{qty: {$lt :10}}, {qty :{$gt: 50}}]},
    {$or: [{sale: true}, {price: {$lt: 5 }}]}
  ]
})

// Element
db.coll.find({name: {$exists: true}})
db.coll.find({"zipCode": {$type: 2 }})
db.coll.find({"zipCode": {$type: "string"}})

// Aggregation Pipeline
db.coll.aggregate([
  {$match: {status: "A"}},
  {$group: {_id: "$cust_id", total: {$sum: "$amount"}}},
  {$sort: {total: -1}}
])

// Text search with a "text" index
db.coll.find({$text: {$search: "cake"}}, {score: {$meta: "textScore"}}).sort({score: {$meta: "textScore"}})

// Regex
db.coll.find({name: /^Max/})   // regex: starts by letter "M"
db.coll.find({name: /^Max$/i}) // regex case insensitive

// Array
db.coll.find({tags: {$all: ["Realm", "Charts"]}})
db.coll.find({field: {$size: 2}}) // impossible to index - prefer storing the size of the array & update it
db.coll.find({results: {$elemMatch: {product: "xyz", score: {$gte: 8}}}})

// Projections
db.coll.find({"x": 1}, {"actors": 1})               // actors + _id
db.coll.find({"x": 1}, {"actors": 1, "_id": 0})     // actors
db.coll.find({"x": 1}, {"actors": 0, "summary": 0}) // all but "actors" and "summary"

// Sort, skip, limit
db.coll.find({}).sort({"year": 1, "rating": -1}).skip(10).limit(3)

// Read Concern
db.coll.find().readConcern("majority")
```

## Delete
```
db.coll.remove({name: "Max"})
db.coll.remove({name: "Max"}, {justOne: true})
db.coll.remove({}) // WARNING! Deletes all the docs but not the collection itself and its index definitions
db.coll.remove({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
db.coll.findOneAndDelete({"name": "Max"})
```

## Databases and Collections
**Drop**
```
db.coll.drop()    // removes the collection and its index definitions
db.dropDatabase() // double check that you are *NOT* on the PROD cluster... :-)
```
**Create Collection**
```
// Create collection with a $jsonschema
db.createCollection("contacts", {
   validator: {$jsonSchema: {
      bsonType: "object",
      required: ["phone"],
      properties: {
         phone: {
            bsonType: "string",
            description: "must be a string and is required"
         },
         email: {
            bsonType: "string",
            pattern: "@mongodb\.com$",
            description: "must be a string and match the regular expression pattern"
         },
         status: {
            enum: [ "Unknown", "Incomplete" ],
            description: "can only be one of the enum values"
         }
      }
   }}
})
```
**Other Collection Functions**
```
db.coll.stats()
db.coll.storageSize()
db.coll.totalIndexSize()
db.coll.totalSize()
db.coll.validate({full: true})
db.coll.renameCollection("new_coll", true) // 2nd parameter to drop the target collection if exists
```