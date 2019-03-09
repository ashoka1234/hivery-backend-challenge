import logging

_LOG = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)


class WriteAPI:
    def __init__(self, db):
        self._db = db
        self._person = db.person
        self._company = db.company

    def init_db(self):
        self._person.remove()
        self._company.remove()

    def add_people(self, people, known_fruits):

        people_data_clean = [self._clean_person_data(person, known_fruits) for person in people]
        self._person.insert_many(people_data_clean)

        _LOG.info('Inserted people: %s', len(people))

    @staticmethod
    def _clean_person_data(person, known_fruits):
        fruits_and_vegies = person.pop("favouriteFood", [])
        fruits = []
        vegies = []
        for food in fruits_and_vegies:
            if food in known_fruits:
                fruits.append(food)
            else:
                vegies.append(food)
        person['fruits'] = fruits
        person['vegetables'] = vegies
        return person

    def add_companies(self, companies):

        self._company.insert_many(companies)

        _LOG.info('Inserted companies: %s', len(companies))
