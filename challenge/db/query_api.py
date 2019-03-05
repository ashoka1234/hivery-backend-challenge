class QueryAPI:
    def __init__(self, db):
        self._db = db
        self._person = db.person
        self._company = db.company

    def get_person(self, person_name, projection):
        return self._person.find_one({"name": person_name}, projection)

    def get_friendship(self, person_name1, person_name2):
        projection = {"name":1, "age":1, "address":1, "phone":1, "friends":1}
        person1 = self._person.find_one({"name": person_name1}, projection)
        person2 = self._person.find_one({"name": person_name2}, projection)
        common_friends = {friend["index"] for friend in person1.get("friends")}.intersection(
            {friend["index"] for friend in person2.get("friends")}
        )
        return [person1, person2, self._alive_brown_eyes(common_friends)]

    def get_company(self, company):
        pass

    def _alive_brown_eyes(self, friends):
        friends_ = self._person.find({"index": {"in": friends}}, {"index":1, "has_died":1, "eyeColor":1})
        return [friend["index"] for friend in friends_ if friend.get("has_died", "") == 'true' and
                friend.get("eyeColor", "") == "brown"]
