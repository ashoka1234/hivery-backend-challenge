import json

FRUITS = {"orange", "apple", "banana", "strawberry"}


class WriteAPI:
    def __init__(self, db):
        self._db = db
        self._person = db.person
        self._company = db.company

    def add_people(self, file):
        with open(file, 'r') as fd:
            people = json.load(fd)
        people_data_clean = [self._clean_person_data(person) for person in people]
        self._person.insert_many(people_data_clean)

    def _clean_person_data(self, person):
        fruits_and_vegies = person.pop("favouriteFood", [])
        fruits = [], vegies = []
        for food in fruits_and_vegies:
            if food in FRUITS:
                fruits.append(food)
            else:
                vegies.append(food)
        person['fruits'] = fruits
        person['vegies'] = vegies
        return person
