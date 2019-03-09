class QueryAPI:
    """
    MongoDB interface for querying person and company collections from a given
    database
    """

    def __init__(self, db):
        self._db = db
        self._person = db.person
        self._company = db.company

    def get_person(self, person_name, projection):
        """
        Return the person having fields defined by the projection (as in mongodb spec)
        """

        return self._person.find_one({"name": person_name}, projection)

    def get_friendship(self, person_name1, person_name2):
        """
        Find common friends who are brown eyes and living
        """

        projection = {"_id":0, "name":1, "age":1, "address":1, "phone":1, "friends":1}

        person1 = self._person.find_one({"name": person_name1}, projection)
        person2 = self._person.find_one({"name": person_name2}, projection)

        if not person1 or not person2:
            return bool(person1), bool(person2), {}

        common_friends = {friend["index"] for friend in person1.get("friends")}.intersection(
            {friend["index"] for friend in person2.get("friends")}
        )

        person1.pop('friends')
        person2.pop('friends')

        return True, True, {'people': [person1, person2], 'friends': self._alive_brown_eyes(common_friends)}

    def get_company(self, company):
        """
        Find employees of a company
        """
        company_ = self._company.find_one({"company": company})

        if not company_:
            return None

        employees = [e for e in self._person.find({"company_id": company_['index']}, {"_id":0, "name":1})]

        return {'company': company, 'employees': employees}

    def _alive_brown_eyes(self, people):
        """
        Which of people (with indices) has brown eyes and living
        """

        people_ = self._person.find({"index": {"$in": list(people)}}, {"index":1, "has_died":1, "eyeColor":1})

        return [person["index"] for person in people_ if not person.get("has_died") and
                person.get("eyeColor", "") == "brown"]
