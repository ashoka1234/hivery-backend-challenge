from challenge.db import QueryAPI


def test_get_person(initialized_db):
    person = QueryAPI(initialized_db).get_person('Carmella Lambert',
                                                 {"_id": 0, "name": 1, "age": 1,
                                                  "fruits": 1, "vegetables":1})
    assert person['age'] == 61

    person = QueryAPI(initialized_db).get_person('Carmella Lambert', {"_id": 0, "name": 1})
    assert person.get('age') is None


def test_get_friendship(initialized_db):
    person1_found, person2_found, result = QueryAPI(initialized_db).get_friendship('Bonnie Bass',
                                                                                   'Mindy Beasley')
    assert person1_found is True
    assert person2_found is True
    assert len(result['friends']) == 1

    person1_found, person2_found, result = QueryAPI(initialized_db).get_friendship('Steve Smith',
                                                                                   'Mindy Beasley')
    assert person1_found is False

    person1_found, person2_found, result = QueryAPI(initialized_db).get_friendship('Bonnie Bass',
                                                                                   'Steve Smith')
    assert person2_found is False


def test_get_compay(initialized_db):
    compay = QueryAPI(initialized_db).get_company('PERMADYNE')
    assert len(compay['employees']) == 7
    assert compay['company'] == 'PERMADYNE'
