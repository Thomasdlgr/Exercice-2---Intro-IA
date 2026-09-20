# Issue #2 — tag_reading accumule des étiquettes d'un appel à l'autre

Niveau : confirmé

## Comportement observé
```python
tag_reading(30)   # ['chaud']
tag_reading(10)   # ['chaud', 'froid']  <- inattendu
```

## Comportement attendu
Chaque appel sans argument `tags` explicite devrait démarrer d'une liste vide :
```python
tag_reading(30)   # ['chaud']
tag_reading(10)   # ['froid']
```

## Indice
Un classique piège Python : un argument par défaut mutable (`tags: list = []`) est créé une
seule fois à la définition de la fonction, et partagé entre tous les appels qui ne le fournissent
pas explicitement.

## Fichier concerné
`toolbox/convert_utils.py`
