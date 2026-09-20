def celsius_to_fahrenheit(celsius: float) -> float:
    """À implémenter : convertit une température de Celsius en Fahrenheit."""
    raise NotImplementedError


def moving_average(values: list, window: int = 3) -> list:
    """À implémenter : renvoie la liste des moyennes glissantes sur `window` éléments."""
    raise NotImplementedError


def tag_reading(value: float, tags: list = []) -> list:
    """Ajoute une étiquette ('chaud' si > 25, sinon 'froid') à tags, et renvoie tags.

    Contient un bug classique de Python à corriger (voir issue #2).
    """
    if value > 25:
        tags.append("chaud")
    else:
        tags.append("froid")
    return tags
