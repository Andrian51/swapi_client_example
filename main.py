from swapi import swapi

def get_film_info(id):
    film = swapi.get_film(id)
    characters = film.get_characters().items

    print(f"Фільм:{film.title}")

print(f"Персонажі:")
for index, character in enumerate(characters, 1):
    print(f"{index} {character.name} з планети (character.get_homeworwd()name)")