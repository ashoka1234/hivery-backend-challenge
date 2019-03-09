from challenge.db import WriteAPI


def test_add_people(empty_db):
    write_db = WriteAPI(empty_db)
    fruits = {"orange", "apple", "banana", "strawberry"}
    people = [
        {
            "_id": "595eeb9b62154a482f446b43",
            "index": 0,
            "guid": "53b032b4-056c-4984-96ef-2b576e5ca1d1",
            "has_died": True,
            "balance": "$3,337.94",
            "picture": "http://placehold.it/32x32",
            "age": 23,
            "eyeColor": "brown",
            "name": "Tricia Stephens",
            "gender": "female",
            "company_id": 15,
            "email": "triciastephens@earthmark.com",
            "phone": "+1 (812) 431-3771",
            "address": "147 Lyme Avenue, Emison, North Carolina, 9596",
            "about": "Cillum culpa amet aliqua anim enim. Esse do dolor irure veniam minim reprehenderit. Ullamco sint labore et enim irure tempor proident culpa duis eu magna. Ea magna ipsum non deserunt cupidatat aliquip ad do. Excepteur proident voluptate pariatur fugiat qui tempor cupidatat ad Lorem.\r\n",
            "registered": "2015-05-29T12:02:46 -10:00",
            "tags": [
                "velit",
                "minim",
                "dolor",
                "id",
                "laboris",
                "veniam",
                "nisi"
            ],
            "friends": [
                {
                    "index": 1
                }
            ],
            "greeting": "Hello, Tricia Stephens! You have 10 unread messages.",
            "favouriteFood": [
                "cucumber",
                "apple",
                "banana",
                "strawberry"
            ]
        }
    ]

    write_db.add_people(people, fruits)
    person = empty_db.person.find_one({"name": "Tricia Stephens"})
    assert person is not None
    assert len(person["fruits"]) == 3
    assert set(person["fruits"]) == {"apple", "banana", "strawberry"}
    assert len(person["vegetables"]) == 1
    assert "cucumber" in person["vegetables"]
