# Issue #1 — is_palindrome renvoie un résultat incorrect sur les chaînes avec espaces

Niveau : standard

## Comportement observé
`is_palindrome("un roc si biscornu")` renvoie `False`.

## Comportement attendu
La fonction devrait ignorer les espaces (et la casse) pour juger si une chaîne est un palindrome.
`is_palindrome("un roc si biscornu")` devrait renvoyer `True`.

## Reproduction
```python
from toolbox.text_utils import is_palindrome
print(is_palindrome("un roc si biscornu"))  # False, attendu : True
```

## Fichier concerné
`toolbox/text_utils.py`
