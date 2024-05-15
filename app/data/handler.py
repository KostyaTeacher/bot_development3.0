import json
from json import JSONDecodeError


def get_films(f_path: str = "app/data/films.json") -> list:
    with open(f_path) as file_json:
        try:
            data = json.load(file_json)
            films = data.get("films")
            return films
        except JSONDecodeError:
            return None


def get_film(id: int = 0, f_path: str = "app/data/films.json") -> dict:
    return get_films(f_path)[id]


def save_film(film: dict = {}, f_path: str = "app/data/films.json") -> bool:
    with open(f_path) as file_json:
        data = json.load(file_json)
        films = data.get("films")
        films.append(film)
    with open(f_path, "w") as file_json:
        json.dump(data, file_json, indent=4)
    return True
